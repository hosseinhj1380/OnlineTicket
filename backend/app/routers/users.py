from fastapi import APIRouter, Depends
from schemas.users import UserBase, UserDisplay, UserUpdate
from crud.users_crud import UserCRUD, check_username
from fastapi.responses import JSONResponse
from core.auth.oauth2 import get_current_user
from core.parameters_check import is_strong_password, is_valid_email

# router = APIRouter(prefix='/user', tags=['user'])
router = APIRouter(prefix="/api/user")


# create user
@router.post("/create", response_model=UserDisplay)
def create_user(user: UserBase):
    if check_username(user.username):
        return JSONResponse(status_code=406, content="username already exist ")

    elif not is_valid_email(user.email):
        return JSONResponse(status_code=406, content="email is not valid ")
    elif user.password is None or user.password in user.username:
        return JSONResponse(
            status_code=406, content="password must not be none or same as username "
        )
    elif not is_strong_password(user.password):
        return JSONResponse(status_code=406, content="password is weak ")
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


# update user
@router.put("/update")
def update_user(user: UserUpdate, current_user: UserBase = Depends(get_current_user)):
    if user:
        if not is_valid_email(user.email):
            return JSONResponse(status_code=406, content="email is not valid ")
        user_obj = UserCRUD()
        result = user_obj.update(user=user.dict(), userID=current_user["userID"])

        if result:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(status_code=400, content=" user not found ")

