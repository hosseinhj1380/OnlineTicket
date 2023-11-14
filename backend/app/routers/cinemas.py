from fastapi import APIRouter, Depends
from schemas.cinemas import Cinema
from fastapi.responses import JSONResponse
from core.auth.oauth2 import oauth2_scheme, is_admin
from crud.cinema_crud import CRUDcinema 
import base64


router = APIRouter(prefix="/api/cinemas")


@router.post("/create" , dependencies=[Depends(is_admin)])
def create_new_cinemas(cinema : Cinema , token: str = Depends(oauth2_scheme) ):
    if cinema :
        #    for movie_picture in movie.movie_images:
        #        try:
        #            decode_image = base64.b64decode(movie_picture)

        #        except:

        #            return JSONResponse(status_code=400, content="movie_images format is not in base64 format ")

        #    try:
        #        decode_image = base64.b64decode(movie.movie_poster)

        #    except:
        #        return JSONResponse(status_code=400, content="movie_poster  format is not in base64 format ")
        obj = CRUDcinema()
        result = obj.create(cinema.dict())
        if result is not None:
            return JSONResponse(status_code= 200  , content= result)
        else:
            
            return JSONResponse (status_code= 406 , content=" cinema with this name already exist ")
            
