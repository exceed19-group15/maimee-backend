from typing import List

from fastapi import APIRouter

from core.database import beatmap
from models.beatmap import Beatmap

router = APIRouter(prefix="/beatmap")


@router.get("/", response_model=List[Beatmap])
async def get_all_beatmap() -> List[Beatmap]:
    return list(beatmap.find({}, {"_id": 0}))


@router.get("/{beatmap_id}/", response_model=Beatmap)
async def get_beatmap(beatmap_id: int) -> Beatmap:
    return beatmap.find_one({"beatmap_id": beatmap_id}, {"_id": 0})
