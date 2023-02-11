from datetime import datetime

from pydantic import BaseModel


class Record(BaseModel):
    username: str
    beatmap_id: int
    score: int
    hit: int
    miss: int
    time: datetime


class LeaderboardRecord(BaseModel):
    username: str
    score: int


class RecordPostModel(BaseModel):
    username: str
    score: int
    hit: int
    miss: int
