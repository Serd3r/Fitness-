from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional

class MembershipType(str, Enum):
    STANDARD = "standard"
    PREMIUM = "premium"
    STUDENT = "student"

class MemberBase(BaseModel):
    name: str
    email: EmailStr
    membership_type: MembershipType = MembershipType.STANDARD

class MemberCreate(MemberBase):
    pass

class MemberRead(MemberBase):
    id: int

    class Config:
        from_attributes = True
