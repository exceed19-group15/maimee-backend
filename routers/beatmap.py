from typing import List

from fastapi import APIRouter

from core.database import beatmap
from models.beatmap import BeatmapInfo


router = APIRouter(prefix="/beatmap")

@router.get("/info/", response_model=List[BeatmapInfo])
async def get_all_beatmap_info() -> List[BeatmapInfo]:
    beatmap_info_list = list(beatmap.find({}, {"_id": 0}))
    for beatmap_info in beatmap_info_list:
        beatmap_info.pop("beats", None)
    return beatmap_info_list


@router.get("/info/{beatmap_id}/", response_model=BeatmapInfo)
async def get_beatmap(beatmap_id: int) -> BeatmapInfo:
    beatmap_info = beatmap.find_one({"beatmap_id": beatmap_id}, {"_id": 0})
    beatmap_info.pop("beats", None)
    return beatmap_info
