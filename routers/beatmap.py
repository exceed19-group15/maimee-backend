from typing import List

from fastapi import APIRouter

from models.beatmap import Beatmap, BeatmapInfo

router = APIRouter(prefix="/beatmap")


@router.get("/info/", response_model=List[BeatmapInfo])
async def get_all_beatmap_info() -> List[BeatmapInfo]:
    pass


@router.get("/info/{beatmap_id}/", response_model=BeatmapInfo)
async def get_beatmap(beatmap_id: int) -> BeatmapInfo:
    pass


@router.get("/", response_model=List[Beatmap])
async def get_all_beatmaps() -> List[Beatmap]:
    pass


@router.get("/{beatmap_id}/", response_model=Beatmap)
async def get_beatmap(beatmap_id: int) -> Beatmap:
    pass
