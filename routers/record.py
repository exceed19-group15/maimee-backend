from typing import List, Dict
from datetime import datetime
from fastapi import APIRouter

from core.database import play_record
from models.record import Record, RecordPutModel

router = APIRouter(prefix="/play-record")


@router.get("/", response_model=List[Record])
async def get_all_play_records() -> List[Record]:
    return list(play_record.find({}, {"_id": 0}))


@router.get("/beatmap/{beatmap_id}/", response_model=List[Record])
async def get_beatmap_play_records(beatmap_id: int) -> List[Record]:
    return play_record.find_one({"beatmap_id": beatmap_id}, {"_id": 0})


@router.put("/beatmap/{beatmap_id}/", response_model=RecordPutModel)
async def put_beatmap_play_record(beatmap_id: int, record: RecordPutModel) -> Dict[str, str]:
    update_body = record.dict()

    for k in tuple(update_body.keys()):
        if update_body[k] is None:
            del update_body[k]

    update_body["time"] = datetime.now()

    play_record.update_one({"beatmap_id": beatmap_id}, {"$set": update_body})
    return {"message": "Update successful"}


@router.get("/user/{username}/", response_model=List[Record])
async def get_user_play_records(username: str) -> List[Record]:
    return list(play_record.find({"username": username}, {"_id": 0}))
