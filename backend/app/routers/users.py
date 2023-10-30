from fastapi import APIRouter
from schemes.users import UserBase,UserDisplay
from app.crud.users_crud import UserCRUD , check_username
from fastapi.responses import JSONResponse

# router = APIRouter(prefix='/user', tags=['user'])
router= APIRouter()


# create user
@router.post('/api/user/', response_model=UserDisplay)
def create_user(user:UserBase):
    if check_username(user.username):
        return JSONResponse(status_code=406,content="username already exist ")
    else:
        new_user=UserCRUD()
        result=new_user.create(username=user.username,email=user.email,password=user.password)
        if isinstance(result,str):
            return JSONResponse(status_code=200,content=result)
        else:
            return JSONResponse(status_code=500,content=result)
    


# read user


# update user


# delete user