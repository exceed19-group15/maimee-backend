from datetime import datetime
from typing import Dict, List

from fastapi import APIRouter

from core.database import play_record
from models.record import Record, RecordPostModel

router = APIRouter(prefix="/play-record")


@router.get("", response_model=List[Record])
async def get_all_play_records() -> List[Record]:
    return list(play_record.find({}, {"_id": 0}))


@router.get("/{beatmap_id}", response_model=List[Record])
async def get_beatmap_play_records(beatmap_id: int) -> List[Record]:
    return list(play_record.find({"beatmap_id": beatmap_id}, {"_id": 0}))


@router.post("/{beatmap_id}", response_model=Dict[str, str])
async def post_beatmap_play_record(
    beatmap_id: int, record: RecordPostModel
) -> Dict[str, str]:
    body = record.dict()
    body["beatmap_id"] = beatmap_id
    body["time"] = datetime.now()
    play_record.insert_one(body)
    return {"message": "success"}
