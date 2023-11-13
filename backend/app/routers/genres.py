from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.genres import Genres, GenresUpdate
from crud.genres_crud import CRUDgenres
from typing import List
from core.auth.oauth2 import is_admin


router = APIRouter(prefix="/api/generes")


@router.post("/create/", dependencies=[Depends(is_admin)])
def create_movies_genres(generes: Genres):
    if generes:
        obj = CRUDgenres()
        result = obj.create_genres(new_genre_name=generes.name)
        if result:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(
                status_code=500, content="internal server error try later "
            )

    else:
        return JSONResponse(status_code=400, content="bad request")


@router.get("/details/")
def get_movies_genres():
    obj = CRUDgenres()

    documents = obj.get_genres_details()

    return JSONResponse(status_code=200, content=list(documents))


@router.put("/update/", dependencies=[Depends(is_admin)])
def update_movie_genres(new_genre: GenresUpdate):
    if new_genre:
        obj = CRUDgenres()
        result = obj.update_genres(
            genres_name=new_genre.name, genres_new_name=new_genre.new_name
        )
        if result == "Successfully Updated ":
            return JSONResponse(status_code=200, content=result)
        elif result == "Failed to update genres":
            return JSONResponse(status_code=500, content=result)
        else:
            return JSONResponse(status_code=404, content=result)


@router.delete("/delete/{genres_name}", dependencies=[Depends(is_admin)])
def delete_movies_genres(genres_name: str):
    obj = CRUDgenres()
    result = obj.delete_genres(genres_name=genres_name)
    if result == "successfully deleted":
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content=result)
