from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from schemas.facilities import Facilities, FacilitiesUpdate
from crud.facilities_crud import FacilitiesCRUD
from typing import List
from core.auth.oauth2 import is_admin


router = APIRouter(prefix="/api/facilities")


@router.post("/create/", dependencies=[Depends(is_admin)])
def create_movies_facility(facilities: Facilities):
    if facilities:
        obj = FacilitiesCRUD()
        result = obj.create_facility(new_facility_name=facilities.name)
        if result:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(
                status_code=500, content="internal server error try later "
            )

    else:
        return JSONResponse(status_code=400, content="bad request")


@router.get("/details/")
def get_movies_facility():
    obj = FacilitiesCRUD()

    documents = obj.get_facility_details()

    return JSONResponse(status_code=200, content=list(documents))


@router.put("/update/", dependencies=[Depends(is_admin)])
def update_movie_facility(new_facilities: FacilitiesUpdate):
    if new_facilities:
        obj = FacilitiesCRUD()
        result = obj.update_facility(
            facility_name=new_facilities.name, facility_new_name=new_facilities.new_name
        )
        if result == "Successfully Updated ":
            return JSONResponse(status_code=200, content=result)
        elif result == "Failed to update facility":
            return JSONResponse(status_code=500, content=result)
        else:
            return JSONResponse(status_code=404, content=result)


@router.delete("/delete/{facility_name}", dependencies=[Depends(is_admin)])
def delete_movies_facility(facility_name: str):
    obj = FacilitiesCRUD()
    result = obj.delete_facility(facility_name=facility_name)
    if result == "successfully deleted":
        return JSONResponse(status_code=200, content=result)
    else:
        return JSONResponse(status_code=404, content=result)
