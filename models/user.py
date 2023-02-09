from datetime import datetime
from typing import List

from pydantic import BaseModel


class PlayRecord(BaseModel):
    song_id: int
    time: datetime
    score: int
    hit: int
    miss: int


class User(BaseModel):
    user_id: int
    username: str
    history: List[PlayRecord]


class UserPassword(BaseModel):
    user_id: int
    password: str  # hashed
