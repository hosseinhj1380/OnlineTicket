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
    description:str
    review:str
    production_year:int
    images:List[str]
    poster:str
    movie_type:str
    genres:List[dict]
    categories:List[dict]



class MovieUpdate(Movies):
    movie_id:int
    


