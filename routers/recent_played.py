from fastapi import APIRouter
from typing import Optional

from models.recent_played import Recent

router = APIRouter(prefix="/Recent")
recent_played_beatmap = None
recent_score = None
recent_hit = None
recent_miss = None


@router.get("/", response_model=Optional[Recent])
async def get_recent() -> Optional[Recent]:
    return Recent(beatmap_id=recent_played_beatmap, score=recent_score, hit=recent_hit, miss=recent_miss)


@router.post("/", response_model=Recent)
async def post_recent(recent: Recent) -> Recent:
    global recent_played_beatmap, recent_score, recent_hit, recent_miss

    recent_played_beatmap = recent.beatmap_id
    recent_score = recent.score
    recent_hit = recent.hit
    recent_miss = recent.miss

    return recent
