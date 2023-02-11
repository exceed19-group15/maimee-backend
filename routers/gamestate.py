from typing import Dict

from fastapi import APIRouter

from constants import FINISHED, MENU, PLAYING
from models.gamestate import GameState

router = APIRouter(prefix="/game-state")

current_game_state = MENU
current_beatmap = None


@router.get("/", response_model=GameState)
async def get_game_state() -> GameState:
    return GameState(game_state=current_game_state, beatmap_id=current_beatmap)


@router.post("/", response_model=Dict[str, str])
async def set_game_state(game_state: GameState) -> Dict[str, str]:

    if game_state.game_state == PLAYING and game_state.beatmap_id is None:
        raise ValueError("beatmap must be set when game_state is PLAYING")

    global current_game_state, current_beatmap
    print(f"game_state: {game_state.game_state}, beatmap: {game_state.beatmap_id}")
    current_game_state = game_state.game_state
    current_beatmap = game_state.beatmap_id

    return {"message": "success"}
