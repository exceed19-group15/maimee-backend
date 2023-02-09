from typing import List

from fastapi import APIRouter

from models.record import Record

router = APIRouter(prefix="/play-record")


@router.get("/", response_model=List[Record])
async def get_all_play_records() -> List[Record]:
    pass


@router.get("/user/{username}", response_model=List[Record])
async def get_user_play_records(username: str) -> List[Record]:
    pass

@router.get("/beatmap/{beatmap_id}", response_model=List[Record])
async def get_beatmap_play_records(beatmap_id: int) -> List[Record]:
    pass
