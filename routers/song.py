from typing import List

from fastapi import APIRouter

from models.song import Song

router = APIRouter(prefix="/song")


@router.get("/", response_model=List[Song])
async def get_all_song() -> List[Song]:
    pass


@router.get("/{song_id}", response_model=Song)
async def get_song(song_id: int) -> Song:
    pass
