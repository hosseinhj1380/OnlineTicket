from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemes.movies import Movies, MovieUpdate
from crud.movies_crud import CRUDmovies

import base64


router = APIRouter()


@router.post("/api/movie/create/")
def create_movie_info(movie: Movies):
    if movie:
        #    for movie_picture in movie.movie_images:
        #        try:
        #            decode_image = base64.b64decode(movie_picture)

        #        except:

        #            return JSONResponse(status_code=400, content="movie_images format is not in base64 format ")

        #    try:
        #        decode_image = base64.b64decode(movie.movie_poster)

        #    except:
        #        return JSONResponse(status_code=400, content="movie_poster  format is not in base64 format ")

        movie_dict = movie.dict()
        obj = CRUDmovies()
        result = obj.create_movie(movie_dict)
        if result["status"] == "Success":
            return JSONResponse(status_code=201, content=result)
        else:
            return JSONResponse(status_code=400, content=result)
    else:
        return JSONResponse(status_code=400, content="bad request (value is null )")


@router.get("/api/movie/movie_datails/{movie_id}")
def get_movie_details(movie_id: int):
    obj = CRUDmovies()
    result = obj.movie_details(movie_id=movie_id)

    if result:
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content="movie not found ")


@router.put("/api/movie/movie_update/")
def movies_update(movie: MovieUpdate):
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
        movie_id = movie.movie_id

    movie_dict = movie.dict()

    obj = CRUDmovies()
    result = obj.movie_update(movie_id=movie_id, movie_info=movie_dict)
    if result == "success":
        return JSONResponse(status_code=204, content="updated successfully")
    elif result == "failed":
        return JSONResponse(
            status_code=500, content="internal server error please try later "
        )
    elif result == "movie_id doesnt exist ":
        return JSONResponse(status_code=404, content="movie_id doesnt exist")


@router.delete("/api/movie/movie_delete/{movie_id}")
def movies_delete(movie_id: int):
    obj = CRUDmovies()
    result = obj.delete_movie(movie_id=movie_id)
    if result == "successfully deleted":
        return JSONResponse(status_code=202, content=result)
    elif result == "movie_id doesnt exist ":
        return JSONResponse(status_code=404, content=result)
