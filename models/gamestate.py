from typing import Optional

from pydantic import BaseModel, validator

from constants import GAME_STATES, PLAYING


class GameState(BaseModel):
    game_state: str
    beatmap_id: Optional[int]
