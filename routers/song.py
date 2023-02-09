from typing import List

from fastapi import APIRouter

from models.song import Song

router = APIRouter(prefix="/song")


@router.get("/")
async def get_all_song() -> List[Song]:
    pass


@router.get("/{song_id}")
async def get_song(song_id: int) -> Song:
    pass
