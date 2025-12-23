from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.fitness_class import FitnessClassCreate, FitnessClassRead
from app.services.class_service import class_service

router = APIRouter(prefix="/classes", tags=["Classes"])

@router.post("/", response_model=FitnessClassRead, status_code=status.HTTP_201_CREATED)
def create_class(fitness_class: FitnessClassCreate):
    return class_service.create_class(fitness_class)

@router.get("/", response_model=List[FitnessClassRead])
def list_classes():
    return class_service.list_classes()

@router.get("/{class_id}", response_model=FitnessClassRead)
def get_class(class_id: int):
    c = class_service.get_class(class_id)
    if not c:
        raise HTTPException(status_code=404, detail="Class not found")
    return c
