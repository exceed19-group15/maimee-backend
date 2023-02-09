from typing import Optional

from pydantic import BaseModel, validator

from constants import GAME_STATES, PLAYING

from .beatmap import Beatmap


class GameState(BaseModel):
    game_state: str
    beatmap_id: Optional[int]

    @validator("game_state")
    def validate_game_state(cls, value, values):
        if value not in GAME_STATES:
            raise ValueError(f"game_state must be one of {GAME_STATES}")
        if value == PLAYING and values["beatmap_id"] is None:
            raise ValueError("beatmap_id must be provided when game_state is PLAYING")
        return value
