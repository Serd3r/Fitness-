from typing import List, Optional
from datetime import datetime
from app.models.fitness_class import FitnessClassCreate, FitnessClassRead

class ClassService:
    def __init__(self):
        self._classes = {}
        self._id_counter = 1

    def create_class(self, class_data: FitnessClassCreate) -> FitnessClassRead:
        class_id = self._id_counter
        # Create class with 0 occupancy initially
        fitness_class = FitnessClassRead(id=class_id, current_occupancy=0, **class_data.model_dump())
        self._classes[class_id] = fitness_class
        self._id_counter += 1
        return fitness_class

    def get_class(self, class_id: int) -> Optional[FitnessClassRead]:
        return self._classes.get(class_id)

    def list_classes(self) -> List[FitnessClassRead]:
        return list(self._classes.values())

class_service = ClassService()
