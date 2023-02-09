from pydantic import BaseModel


class Song(BaseModel):
    song_id: int
    file_name: str
    name: str
    artist: str
    difficulty: int
    note_count: int
    bpm: int
