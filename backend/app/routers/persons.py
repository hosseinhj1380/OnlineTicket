from fastapi import APIRouter , Depends
from fastapi.responses import JSONResponse
from schemas.person import Person,PersonRole
from crud.persons_crud import PersonsCRUD,PersonRoleCRUD
from core.auth.oauth2 import is_admin

router = APIRouter(prefix="/api/person")


@router.post("/" , dependencies=[Depends(is_admin)])
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
        # return result 
        if result["status"]=="success":
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=500,content=result)
        
@router.get("/{PersonID}")
def get_person(PersonID:int):
    if PersonID:
        person_info=PersonsCRUD()
        result=person_info.get(PersonID)
        if result:
            return JSONResponse (status_code=200,content=result)
        else:return JSONResponse(status_code=400,content="person is not defined ")
        
@router.patch("/" , dependencies=[Depends(is_admin)])
def update_person(PersonId:int,person:Person):
    if person:
        person_update=PersonsCRUD()
        result=person_update.update(PersonID=PersonId,PersonInfo=person.dict())
        if result is not None:
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=400,content="person is not found ")
        
@router.delete("/{PersonID}" , dependencies=[Depends(is_admin)])
def delete_person(PersonId:int):
    if PersonId:
        person_update=PersonsCRUD()
        result=person_update.delete(PersonID=PersonId)
        if result is not None:
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=400,content="person is not found ")
        

@router.post("/role" , dependencies=[Depends(is_admin)])
def create_person_role(role:PersonRole):
    new_role=PersonRoleCRUD()
    
    return JSONResponse(status_code=200,content=new_role.create(role.name))


@router.get("/role/" , dependencies=[Depends(is_admin)])
def get_person_role():
    roles=PersonRoleCRUD()
    return JSONResponse(status_code=200,content=roles.get())
