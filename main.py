from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers import beatmap, gamestate, user

app = FastAPI()

app.include_router(gamestate.router)
app.include_router(beatmap.router)
app.include_router(user.router)

@app.exception_handler(ValueError)
def handle_value_error(_, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )