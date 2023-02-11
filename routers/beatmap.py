from typing import List, Optional

from fastapi import APIRouter, HTTPException

from core.database import beatmap
from models.beatmap import Beatmap

router = APIRouter(prefix="/beatmap")


@router.get("/", response_model=List[Beatmap])
async def get_all_beatmap() -> List[Beatmap]:
    return list(beatmap.find({}, {"_id": 0}))


@router.get("/{beatmap_id}", response_model=Optional[Beatmap])
async def get_beatmap(beatmap_id: int) -> Optional[Beatmap]:
    res = beatmap.find_one({"beatmap_id": beatmap_id}, {"_id": 0})
    if res is None:
        raise HTTPException(status_code=404, detail="beatmap not found")
    return res
