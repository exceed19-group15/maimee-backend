from typing import Dict, Optional

from fastapi import APIRouter

from models.recent_played import Recent

router = APIRouter(prefix="/recent")
recent_played_beatmap = None
recent_score = None
recent_hit = None
recent_miss = None


@router.get("", response_model=Optional[Recent])
async def get_recent() -> Optional[Recent]:
    if (
        recent_played_beatmap is None
        or recent_score is None
        or recent_hit is None
        or recent_miss is None
    ):
        return None
    return Recent(
        beatmap_id=recent_played_beatmap,
        score=recent_score,
        hit=recent_hit,
        miss=recent_miss,
    )


@router.post("", response_model=Dict[str, str])
async def post_recent(recent: Recent) -> Dict[str, str]:
    global recent_played_beatmap, recent_score, recent_hit, recent_miss

    recent_played_beatmap = recent.beatmap_id
    recent_score = recent.score
    recent_hit = recent.hit
    recent_miss = recent.miss

    return {"message": "success"}
