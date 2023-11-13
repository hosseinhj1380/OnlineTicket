from pydantic import BaseModel
from typing import List


class Movies(BaseModel):
    title: str
    # movie_pictures:List[UploadFile]
    # movie_poster:UploadFile
    producers: List[int]
    directors: List[int]
    actors: List[int]
    description: str
    review: str
    production_year: int
    images: List[str]
    poster: str
    movie_type: str
    genres: List[dict]
    categories: List[dict]


class MovieUpdate(Movies):
    movie_id: int
