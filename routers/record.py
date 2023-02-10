from typing import List, Dict
from datetime import datetime
from fastapi import APIRouter

from core.database import play_record
from models.record import Record, RecordPostModel

router = APIRouter(prefix="/play-record")


@router.get("/", response_model=List[Record])
async def get_all_play_records() -> List[Record]:
    return list(play_record.find({}, {"_id": 0}))


@router.get("/beatmap/{beatmap_id}/", response_model=List[Record])
async def get_beatmap_play_records(beatmap_id: int) -> List[Record]:
    return play_record.find_one({"beatmap_id": beatmap_id}, {"_id": 0})


@router.post("/beatmap/{beatmap_id}/", response_model=RecordPostModel)
async def post_beatmap_play_record(beatmap_id: int, record: RecordPostModel) -> Dict[str, str]:
    posting_body = record.dict()

    for k in tuple(posting_body.keys()):
        if posting_body[k] is None:
            del posting_body[k]

    posting_body["beatmap_id"] = beatmap_id
    posting_body["time"] = datetime.now()

    play_record.update_one({"beatmap_id": beatmap_id}, {"$set": posting_body})
    return {"message": f"Posted {posting_body}"}


@router.get("/user/{username}/", response_model=List[Record])
async def get_user_play_records(username: str) -> List[Record]:
    return list(play_record.find({"username": username}, {"_id": 0}))
