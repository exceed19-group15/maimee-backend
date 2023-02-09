from typing import List

from fastapi import APIRouter

from models.beatmap import Beatmap

router = APIRouter(prefix="/beatmap")


@router.get("/", response_model=List[Beatmap])
async def get_all_beatmap() -> List[Beatmap]:
    pass


@router.get("/{beatmap_id}", response_model=Beatmap)
async def get_beatmap(beatmap_id: int) -> Beatmap:
    pass
