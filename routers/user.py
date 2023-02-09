from typing import List

from fastapi import APIRouter

from models.user import PlayRecord, User, UserPassword

router = APIRouter(prefix="/user")


@router.get("/{user_id}")
async def get_user(user_id: int) -> User:
    pass


@router.get("/{user_id}/history")
async def get_user_history(user_id: int) -> List[PlayRecord]:
    pass


@router.post("/validate")
async def validate_user(UserPassword: UserPassword) -> bool:
    pass
