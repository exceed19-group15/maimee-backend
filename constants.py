import os
from dotenv import load_dotenv

MENU = "MENU"
PLAYING = "PLAYING"
FINISHED = "FINISHED"

GAME_STATES = [MENU, PLAYING, FINISHED]


load_dotenv()

MONGO_DB_USERNAME = os.getenv("MONGO_DB_USERNAME")
MONGO_DB_PASSWORD = os.getenv("MONGO_DB_PASSWORD")
MONGO_DB_HOST = os.getenv("MONGO_DB_HOST")
MONGO_DB_PORT = os.getenv("MONGO_DB_PORT")
