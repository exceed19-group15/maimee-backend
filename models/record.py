from datetime import datetime
from pydantic import BaseModel


class Record(BaseModel):
    username: str
    beatmap_id: int
    score: int
    hit: int
    miss: int
    time: datetime


class RecordPostModel(BaseModel):
    username: str
    score: int
    hit: int
    miss: int
