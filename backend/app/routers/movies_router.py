from fastapi import APIRouter,UploadFile,status
from fastapi.responses import JSONResponse
from schemes.movies_schemas import Movies,movie_get
# from dependencies import get_db
from crud.movies_crud import CRUDmovies
from typing import List
import base64
from databases import MongoClient
import json

router = APIRouter()


@router.post("/api/movie/create/")
def create_movie_info(movie:Movies):

    if movie:

        # for movie_picture in  movie.movie_images:
        #     try:
        #         decode_image=base64.b64decode(movie_picture)

        #     except:

        #         return JSONResponse(status_code=400,content="movie_images format is not in base64 format ")
            
        # try:
        #     decode_image=base64.b64decode(movie.movie_poster)

        # except:
        #         return JSONResponse(status_code=400,content="movie_poster  format is not in base64 format ")
        
        movie_dict=movie.dict()
        obj=CRUDmovies
        obj.create_movie(movie_dict)

        return JSONResponse (status_code=201,content="created successfully ")

    else:
         
         return JSONResponse (status_code=400 ,content="bad request (value is null )")
    



@router.get("/api/movie/movie_datails/{movie_id}")
def movie_details(movie_id:int):
     
     obj=CRUDmovies
     result=obj.movie_details(movie_id=movie_id)

     if result:
          return JSONResponse(status_code=200 , content=result)
     else:
          return JSONResponse(status_code=404, content="movie not found ")

#    
     

     



    

    

    













    
    