from pydantic import BaseModel
from typing import List
from fastapi import UploadFile,Form



class Movies(BaseModel):

    title:str
    # movie_pictures:List[UploadFile]
    # movie_poster:UploadFile
    producer_name:str
    director_name:str
    actors_name:List[str]
    movie_description:str
    movie_review:str
    production_year:int
    movie_images:List[str]
    movie_poster:str
    movie_type:str



class MovieUpdate(Movies):
    movie_id:int
    


