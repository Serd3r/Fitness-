from pydantic import BaseModel, FutureDatetime
from datetime import datetime
from typing import Optional

class FitnessClassBase(BaseModel):
    name: str
    instructor: str
    capacity: int
    start_time: datetime
    price: float = 20.0  # Base price

class FitnessClassCreate(FitnessClassBase):
    pass

class FitnessClassRead(FitnessClassBase):
    id: int
    current_occupancy: int = 0

    class Config:
        from_attributes = True
