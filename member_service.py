from typing import List, Optional
from app.models.member import MemberCreate, MemberRead

class MemberService:
    def __init__(self):
        self._members = {}
        self._id_counter = 1

    def create_member(self, member_data: MemberCreate) -> MemberRead:
        member_id = self._id_counter
        member = MemberRead(id=member_id, **member_data.model_dump())
        self._members[member_id] = member
        self._id_counter += 1
        return member

    def get_member(self, member_id: int) -> Optional[MemberRead]:
        return self._members.get(member_id)

    def list_members(self) -> List[MemberRead]:
        return list(self._members.values())

# Global instance for simplicity in this demo (in real app, use dependency injection)
member_service = MemberService()
