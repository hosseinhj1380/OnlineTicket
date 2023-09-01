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
    has_been_sold:int = 0
    movie_rate:int=0
    


class movie_get(Movies):
    id:int
    movie_rate:int = 0 
    sale:int


