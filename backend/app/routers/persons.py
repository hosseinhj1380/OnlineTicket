from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemes.person import Person
from crud.persons_crud import PersonsCRUD


router = APIRouter()


@router.post("/api/person/")
def create_person(person:Person):
    if person:
    #    for person_image in person.images:
     #        try:
     #            decode_image = base64.b64decode(person_image)

     #        except:

     #            return JSONResponse(status_code=400, content="person_image format is not in base64 format ")

     #    try:
     #        decode_image = base64.b64decode(person.profile_photo)

     #    except:
     #        return JSONResponse(status_code=400, content="person_image  format is not in base64 format ")
        new_person=PersonsCRUD()
        result=new_person.create(person.dict())
        
        if result["status"]=="success":
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=500,content=result)
        
@router.get("/api/person/{PersonID}")
def get_person(PersonID:int):
    if PersonID:
        person_info=PersonsCRUD()
        result=person_info.get(PersonID)
        if result:
            return JSONResponse (status_code=200,content=result)
        else:return JSONResponse(status_code=400,content="person is not defined ")
        
@router.patch("/api/person/")
def update_person(PersonId:int,person:Person):
    if person:
        person_update=PersonsCRUD()
        result=person_update.update(PersonID=PersonId,PersonInfo=person.dict())
        if result is not None:
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=400,content="person is not found ")
        
@router.delete("/api/person/{PersonID}")
def delete_person(PersonId:int):
    if PersonId:
        person_update=PersonsCRUD()
        result=person_update.delete(PersonID=PersonId)
        if result is not None:
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=400,content="person is not found ")