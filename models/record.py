from datetime import datetime
from typing import List

from pydantic import BaseModel


class PlayRecord(BaseModel):
    username: str
    beatmap_id: int
    score: int
    hit: int
    miss: int
    time: datetime