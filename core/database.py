from pymongo import MongoClient

from constants import *

client = MongoClient(
    f"mongodb://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}"
)

db = client["exceed15"]

if "play_record" not in db.list_collection_names():
    db.create_collection("play_record")

play_record = db["play_record"]

if "beatmap" not in db.list_collection_names():
    db.create_collection("beatmap")

beatmap = db["beatmap"]
