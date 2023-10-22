from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemes.person import Person
from crud.persons_crud import PersonsCRUD


router = APIRouter()


@router.post("/api/person/")
def create_person(person:Person):
    if person:
        new_person=PersonsCRUD()
        result=new_person.create(person.dict())
        
        if result["status"]=="success":
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=500,content=result)