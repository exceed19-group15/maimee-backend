from typing import Any, Dict, List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from core.database import play_record
from models.record import LeaderboardRecord

router = APIRouter(prefix="/leaderboard")


@router.get("/{beatmap_id}", response_model=List[LeaderboardRecord])
async def get_leaderboard(
    beatmap_id: int, limit: Optional[int] = None
) -> List[LeaderboardRecord]:

    aggregation: List[Dict[str, Any]] = [
        {
            "$match": {
                "beatmap_id": beatmap_id,
            }
        },
        {
            "$group": {
                "_id": "$username",
                "score": {"$max": "$score"},
            }
        },
        {
            "$addFields": {
                "username": "$_id",
            }
        },
        {"$project": {"_id": 0}},
    ]

    if limit is not None:
        if limit <= 0:
            raise ValueError("limit must be greater than 0")
        aggregation.append({"$limit": limit})

    aggregation.append({"$sort": {"score": -1}})

    return list(play_record.aggregate(aggregation))
