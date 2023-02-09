from fastapi import FastAPI

from routers import game_state, song, user

app = FastAPI()

app.include_router(game_state.router)
app.include_router(song.router)
app.include_router(user.router)
