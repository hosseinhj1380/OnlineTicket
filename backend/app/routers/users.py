from fastapi import APIRouter, Depends
from schemas.users import UserBase, UserDisplay
from crud.users_crud import UserCRUD, check_username
from fastapi.responses import JSONResponse
from core.auth.oauth2 import oauth2_scheme

# router = APIRouter(prefix='/user', tags=['user'])
router = APIRouter(prefix="/api/user")


# create user
@router.post("/create", response_model=UserDisplay)
def create_user(user: UserBase):
    if check_username(user.username):
        return JSONResponse(status_code=406, content="username already exist ")
    else:
        new_user = UserCRUD()
        result = new_user.create(
            username=user.username,
            email=user.email,
            password=user.password,
            full_name=user.full_name,
        )
        if isinstance(result, str):
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(status_code=500, content=result)


# read user


# update user


# delete user
