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

    


class movie_get(BaseModel):
    movie_id:int
    # movie_rate:dict  
    # has_been_sold:int
    


