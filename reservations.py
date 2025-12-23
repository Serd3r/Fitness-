from fastapi import APIRouter, status, Response
from typing import List
from app.models.reservation import ReservationCreate, ReservationRead
from app.services.reservation_service import reservation_service

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=ReservationRead, status_code=status.HTTP_201_CREATED)
def create_reservation(reservation: ReservationCreate):
    return reservation_service.create_reservation(reservation)

@router.delete("/{reservation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_reservation(reservation_id: int):
    reservation_service.cancel_reservation(reservation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/", response_model=List[ReservationRead])
def list_reservations():
    return reservation_service.list_reservations()
