from fastapi import APIRouter

from constants import FINISHED, MENU, PLAYING
from models.gamestate import GameState

router = APIRouter(prefix="/game-state")

current_game_state = MENU
current_beatmap = None


@router.get("/", response_model=GameState)
async def get_game_state() -> GameState:
    return GameState(game_state=current_game_state, beatmap=current_beatmap)


@router.post("/", response_model=GameState)
async def set_game_state(game_state: GameState) -> GameState:
    global current_game_state, current_beatmap

    if game_state.game_state == PLAYING and game_state.beatmap is None:
        raise ValueError("beatmap must be set when game_state is PLAYING")

    current_game_state = game_state.game_state
    current_beatmap = game_state.beatmap

    return game_state
