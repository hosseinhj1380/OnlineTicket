from fastapi import Depends, APIRouter, Query,UploadFile,Form,File

from schemes.movies_schemas import Movies,movie_get
# from dependencies import get_db
from crud.movies_crud import CRUDmovies
from typing import List

from databases import MongoClient

router = APIRouter()


@router.post("/api/movie/create/")
def create_comment(movie:Movies=Depends (),
                   movie_images:List[UploadFile]=File(...),
                   movie_poster:UploadFile=File(...)):
    # movie_dict=movie.dict()

    # obj=CRUDmovies
    # obj.create_movie(movie_dict)

    with open(f"../../backend/static/movie_images/{movie_images[0].filename}", "wb") as f:
            f.write(movie_images[0].file.read())

    


# @router.










    
    