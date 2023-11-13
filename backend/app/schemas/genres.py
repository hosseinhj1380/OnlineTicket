from pydantic import BaseModel


class Genres(BaseModel):
    name: str


class GenresUpdate(Genres):
    new_name: str
