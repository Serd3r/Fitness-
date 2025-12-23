from pydantic import BaseModel
from typing import Optional

class ReservationBase(BaseModel):
    member_id: int
    class_id: int

class ReservationCreate(ReservationBase):
    pass

class ReservationRead(ReservationBase):
    id: int
    price_paid: float
    status: str = "confirmed"

    class Config:
        from_attributes = True
