from typing import Optional

from pydantic import BaseModel, validator

from constants import GAME_STATES

from .song import Song


class GameState(BaseModel):
    game_state: str
    song: Optional[Song]

    @validator("game_state")
    def validate_game_state(game_state):
        if game_state not in GAME_STATES:
            raise ValueError(
                f"Invalid game state: {game_state}. Should be one of MENU, PLAYING, or FINISHED."
            )
        return game_state

    def __str__(self):
        return f"GameState(game_state={self.game_state}, song={self.song})"
