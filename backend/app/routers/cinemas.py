
from fastapi import APIRouter, Depends, status, Query
from schemas.cinemas import Cinema
from fastapi.responses import JSONResponse
from core.auth.oauth2 import oauth2_scheme, is_admin
from crud.cinema_crud import CRUDcinema
import base64
from core.parameters_check import is_valid_number_cinema
from fastapi.exceptions import (
    ValidationException,
    HTTPException,
    RequestValidationError,
)
import requests

router = APIRouter(prefix="/api/cinemas")

GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your actual API key



@router.post("/create/" , dependencies=[Depends(is_admin)])
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


        if is_valid_number_cinema(cinema.telephones):
            obj = CRUDcinema()
            result = obj.create(cinema.dict())
            if result is not None:
                return JSONResponse(status_code=200, content=result)
            else:
                return JSONResponse(
                    status_code=406, content=" cinema with this name already exist "
                )
        else:
            return ValidationException(errors="telephones with this format is incorect")


@router.patch("/edit/{cinemaID}", dependencies=[Depends(is_admin)])
def edit_cinema(cinemaID: int, cinema: Cinema, token: str = Depends(oauth2_scheme)):
    if cinema:
        update_cinema = CRUDcinema()
        result = update_cinema.update(cinemaID=cinemaID, cinema=cinema.dict())
        if update_cinema is not None:
            return JSONResponse(status_code=202, content=result)
        else:
            return " cinema with this ID is not available "


@router.get("/{cinemaID}", dependencies=[Depends(is_admin)])
def show_cinema_info(cinemaID: int, token: str = Depends(oauth2_scheme)):
    i = CRUDcinema()
    info = i.get(cinemaID)
    if info is not None:
        return JSONResponse(status_code=200, content=info)
    else:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid cinemaID"
        )


def get_lat_long(location: str) -> dict:
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": location, "key": GOOGLE_MAPS_API_KEY}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data["status"] == "OK":
        result = data["results"][0]["geometry"]["location"]
        return result
    else:
        raise HTTPException(status_code=400, detail="Failed to geocode location")


@router.get("/get_coordinates")
async def get_coordinates(location: str = Query(..., title="Location to geocode")):
    coordinates = get_lat_long(location)
    return {"location": location, "coordinates": coordinates}



