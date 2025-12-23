from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.member import MemberCreate, MemberRead
from app.services.member_service import member_service

router = APIRouter(prefix="/members", tags=["Members"])

@router.post("/", response_model=MemberRead, status_code=status.HTTP_201_CREATED)
def create_member(member: MemberCreate):
    # Basic check for duplicate email could go here
    return member_service.create_member(member)

@router.get("/{member_id}", response_model=MemberRead)
def get_member(member_id: int):
    member = member_service.get_member(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@router.get("/", response_model=List[MemberRead])
def list_members():
    return member_service.list_members()
