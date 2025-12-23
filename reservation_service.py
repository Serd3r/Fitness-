from typing import List, Optional
from fastapi import HTTPException
from app.models.reservation import ReservationCreate, ReservationRead
from app.services.member_service import member_service
from app.services.class_service import class_service
from app.services.pricing_engine import pricing_engine

class ReservationService:
    def __init__(self):
        self._reservations = {}
        self._id_counter = 1

    def create_reservation(self, reservation_data: ReservationCreate) -> ReservationRead:
        # Validate Member
        member = member_service.get_member(reservation_data.member_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")

        # Validate Class
        fitness_class = class_service.get_class(reservation_data.class_id)
        if not fitness_class:
            raise HTTPException(status_code=404, detail="Class not found")

        # Check Capacity
        if fitness_class.current_occupancy >= fitness_class.capacity:
            raise HTTPException(status_code=400, detail="Class is full")

        # Calculate Price
        occupancy_rate = fitness_class.current_occupancy / fitness_class.capacity if fitness_class.capacity > 0 else 1.0
        price = pricing_engine.calculate_price(
            base_price=fitness_class.price,
            membership_type=member.membership_type,
            occupancy_rate=occupancy_rate,
            class_time=fitness_class.start_time
        )

        # Create Reservation
        res_id = self._id_counter
        reservation = ReservationRead(
            id=res_id,
            price_paid=price,
            **reservation_data.model_dump()
        )
        self._reservations[res_id] = reservation
        self._id_counter += 1

        # Update Class Occupancy
        fitness_class.current_occupancy += 1

        return reservation

    def cancel_reservation(self, reservation_id: int):
        reservation = self._reservations.get(reservation_id)
        if not reservation:
            raise HTTPException(status_code=404, detail="Reservation not found")

        # Update Class Occupancy
        fitness_class = class_service.get_class(reservation.class_id)
        if fitness_class and fitness_class.current_occupancy > 0:
            fitness_class.current_occupancy -= 1

        del self._reservations[reservation_id]

    def list_reservations(self) -> List[ReservationRead]:
        return list(self._reservations.values())

reservation_service = ReservationService()
