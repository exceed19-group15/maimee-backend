from typing import List

from pydantic import BaseModel, validator


class Beat(BaseModel):
    pad_num: int
    timestamp: int
    frequency: int

    @validator("pad_num")
    def validate_pad_num(cls, value):
        if value not in range(0, 4):
            raise ValueError("pad_num must be between 0 and 3")
        return value

    @validator("timestamp")
    def validate_timestamp(cls, value):
        if value < 0:
            raise ValueError("timestamp must be greater than 0")
        return value

    @validator("frequency")
    def validate_frequency(cls, value):
        if value < 50 or value > 14000:
            raise ValueError("frequency must be between 50 and 14000")
        return value


class BeatmapInfo(BaseModel):
    beatmap_id: int
    name: str
    difficulty: int
    note_count: int
    bpm: int
    duration: int

    @validator("difficulty")
    def validate_difficulty(cls, value):
        if value not in range(1, 11):
            raise ValueError("difficulty must be between 1 and 10")
        return value

    @validator("note_count")
    def validate_note_count(cls, value):
        if value < 0:
            raise ValueError("note_count must be greater than 0")
        return value

    @validator("bpm")
    def validate_bpm(cls, value):
        if value < 0:
            raise ValueError("bpm must be greater than 0")
        return value

    @validator("duration")
    def validate_duration(cls, value):
        if value < 0:
            raise ValueError("duration must be greater than 0")
        return value


class Beatmap(BeatmapInfo):
    beats: List[Beat]

    @validator("beats")
    def validate_beats(cls, value):
        if len(value) == 0:
            raise ValueError("beats must not be empty")
        return value
