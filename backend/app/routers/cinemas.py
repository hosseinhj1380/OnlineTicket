from fastapi import APIRouter, Depends, status, Query
from schemas.cinemas import Cinema, Halls, Session, UpdateSession
from fastapi.responses import JSONResponse
from core.auth.oauth2 import oauth2_scheme, is_admin , is_cinemaagent_or_admin
from crud.cinema_crud import CRUDcinema, CRUDhalls, CRUDsession
import base64
from core.parameters_check import (
    is_valid_number_cinema,
    is_valid_format,
    is_valid_time_format,
)
from fastapi.exceptions import (
    ValidationException,
    HTTPException,
)
import requests


router = APIRouter(prefix="/api/cinemas")

GOOGLE_MAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your actual API key


@router.post("/create/", dependencies=[Depends(is_cinemaagent_or_admin )])
def create_new_cinemas(cinema: Cinema, token: str = Depends(oauth2_scheme)):
    if cinema:
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


@router.patch("/edit/{cinemaID}", dependencies=[Depends(is_cinemaagent_or_admin )])
def edit_cinema(cinemaID: int, cinema: Cinema, token: str = Depends(oauth2_scheme)):
    if cinema:
        update_cinema = CRUDcinema()
        result = update_cinema.update(cinemaID=cinemaID, cinema=cinema.dict())
        if update_cinema is not None:
            return JSONResponse(status_code=202, content=result)
        else:
            return " cinema with this ID is not available "


@router.get("/{cinemaID}", dependencies=[Depends(is_cinemaagent_or_admin)])
def show_cinema_info(cinemaID: int, token: str = Depends(oauth2_scheme)):
    i = CRUDcinema()
    info = i.get(cinemaID)
    if info is not None:
        return JSONResponse(status_code=200, content=info)
    else:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid cinemaID"
        )


@router.post("/halls/{cinemaID}", dependencies=[Depends(is_cinemaagent_or_admin )])
def create_new_hall(cinemaID: int, hall: Halls, token: str = Depends(oauth2_scheme)):
    if hall:
        c = CRUDhalls()
        result = c.create(cinemaID=cinemaID, hall=hall.dict())
        if result is not None:
            return JSONResponse(status_code=200, content=result)
        else:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="invalid cinemaID"
            )


@router.patch("/hall/{cinemaID}/{hallID}", dependencies=[Depends(is_cinemaagent_or_admin )])
def update_hall(
    cinemaID: int, hallID: int, hall: Halls, token: str = Depends(oauth2_scheme)
):
    if hall:
        u = CRUDhalls()
        result = u.update(hall=hall.dict(), hallID=hallID, cinemaID=cinemaID)

        if result is not None:
            return JSONResponse(status_code=202, content=result)
        else:
            return HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="invalid cinemaID or hallid ",
            )


@router.get("/hall/{cinemaID}", dependencies=[Depends(  is_cinemaagent_or_admin)])
def get_halls_info(cinemaID: int, token: str = Depends(oauth2_scheme)):
    g = CRUDhalls()
    result = g.get(cinemaID=cinemaID)
    if result:
        return JSONResponse(status_code=200, content=list(result))
    else:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid cinemaID  "
        )


@router.get("/hall/{cinemaID}/{hallID}", dependencies=[Depends(is_cinemaagent_or_admin )])
def get_a_hall_info(cinemaID: int, hallID: int, token: str = Depends(oauth2_scheme)):
    g = CRUDhalls()
    result = g.get(cinemaID=cinemaID, hallID=hallID)
    if result:
        return JSONResponse(status_code=200, content=result)
    else:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid cinemaID or hallID "
        )


@router.post("/session/{cinemaID}/{hallID}", dependencies=[Depends(is_cinemaagent_or_admin )])
def new_session(
    cinemaID: int, hallID: int, session: Session, token: str = Depends(oauth2_scheme)
):
    if session:
        if (
            is_valid_format(session.start_release_date)
            and is_valid_format(session.end_release_date)
            and is_valid_time_format(session.start_at)
        ):
            s = CRUDsession()
            result = s.create(cinemaID, hallID, session.dict())
            if result is not None:
                return JSONResponse(status_code=200, content=result)

            else:
                return HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="invalid cinemaID or hallID ",
                )
        else:
            return JSONResponse(status_code=406, content="wrong format datetime ")


@router.patch("/session", dependencies=[Depends(is_cinemaagent_or_admin )])
def update_sessions(session: UpdateSession, token: str = Depends(oauth2_scheme)):
    if session:
        if (
            is_valid_format(session.start_release_date)
            and is_valid_format(session.end_release_date)
            and is_valid_time_format(session.start_at)
        ):
            u = CRUDsession()
            result = u.update(session.dict())
            if result is not None:
                return JSONResponse(status_code=200, content=result)

            else:
                return HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="invalid sessionID ",
                )
        else:
            return JSONResponse(status_code=406, content="wrong format datetime ")


# @router.delete("/session/{sessionID}", dependencies=[Depends(is_cinemaagent_or_admin)])
# def update_sessions( sessionID : int , token: str = Depends(oauth2_scheme)
# ):
#     d = CRUDhalls()
#     result=d.delete_session(sessionID)
#     if result is not None:
#                 return JSONResponse(status_code=200, content=result)

#     else:
#         return HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="invalid cinemaID or hallID ",
#         )



@router.get("/detail/{cinemaID}")
def get_cinema_info(cinemaID: int):
    g = CRUDcinema()
    result = g.get_a_cinema_details(cinemaID=cinemaID)
    if result is not None:
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content="cinemaID is not valid ")


@router.get("/home/")
def cinemas_home(city :int ,page: int = Query(default=1, description="Page number", ge=1)
):
    page_size = 20
    skip = (page - 1) * page_size
    
    c = CRUDcinema()
    result =c.home_cinemas(skip=skip , page_size=page_size  , city=city)
    
    if result["results"] == []:
        return JSONResponse(status_code=404, content="invalid page")

    else:
        if page == 1:
            previous = None
        else:
            previous = (
                f"127.0.0.1:8000/api/cinema/home/?city={city}&page={page - 1}"
            )

        if page_size * page < result["count"]:
            next = (
                f"127.0.0.1:8000/api/comment/comments/?city={city}&page={page + 1}"
            )

        else:
            next = None

        return JSONResponse(
            status_code=200,
            content={
                "count": result["count"],
                "previous": previous,
                "next": next,
                "results": result["results"],
            },
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
