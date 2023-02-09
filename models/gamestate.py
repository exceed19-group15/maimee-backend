from typing import Optional

from pydantic import BaseModel, validator

from constants import GAME_STATES, PLAYING

from .beatmap import Beatmap


class GameState(BaseModel):
    game_state: str
    beatmap: Optional[Beatmap]

    @validator("game_state")
    def validate_game_state(cls, value, values):
        if value not in GAME_STATES:
            raise ValueError("game_state must be one of: " + ", ".join(GAME_STATES))
        
        if value == PLAYING and values.get("beatmap") is None:
            raise ValueError("beatmap must be set when game_state is PLAYING")
        
        return value