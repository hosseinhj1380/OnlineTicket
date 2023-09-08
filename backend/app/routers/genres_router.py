from fastapi import APIRouter, UploadFile, status
from fastapi.responses import JSONResponse
from schemes.genres_schemas import Genres
from crud.genres_crud import CRUDgenres
from typing import List
import base64
from databases import MongoClient
import json

router = APIRouter()


@router.post("/api/generes/create/")
def create_movies_genres(generes:Genres):
    if generes:

        obj=CRUDgenres()
        result=obj.create_genres(new_genre_name=generes.name)
        if result:
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=500,content="internal server error try later ")
        
    else:

        return JSONResponse(status_code=400,content="bad request")
    
@router.get("/api/generes/details/")
def get_movies_genres():

    obj=CRUDgenres()

    documents=obj.get_genres_details()

    
    return JSONResponse(status_code=200,content=list(documents)) 
