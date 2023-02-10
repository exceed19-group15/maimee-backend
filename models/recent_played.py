from pydantic import BaseModel


class Recent(BaseModel):
    beatmap_id: int
    score: int
    hit: int
    miss: int
