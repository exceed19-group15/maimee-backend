from typing import List

from fastapi import APIRouter

from models.user import PlayRecord, User, UserPassword

router = APIRouter(prefix="/user")


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int) -> User:
    pass


@router.get("/{user_id}/history", response_model=List[PlayRecord])
async def get_user_history(user_id: int) -> List[PlayRecord]:
    return []


@router.post("/validate", response_model=bool)
async def validate_user(UserPassword: UserPassword) -> bool:
    return False
