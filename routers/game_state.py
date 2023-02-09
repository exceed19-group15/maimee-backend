from fastapi import APIRouter

from constants import FINISHED, MENU, PLAYING
from models.game_state import GameState

router = APIRouter(prefix="/game_state")

current_game_state = MENU
current_song = None


@router.get("/", response_model=GameState)
async def get_game_state() -> GameState:
    pass


@router.post("/", response_model=GameState)
async def set_game_state(game_state: GameState) -> GameState:
    pass
