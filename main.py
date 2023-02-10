from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from routers import beatmap, gamestate, record

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(gamestate.router)
app.include_router(beatmap.router)
app.include_router(record.router)


@app.exception_handler(ValueError)
def handle_value_error(_, exc):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )
