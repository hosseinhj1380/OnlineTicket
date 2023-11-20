from fastapi import APIRouter, Depends
from schemas.users import UserBase, UserDisplay, UserUpdate
from crud.users_crud import UserCRUD, check_username, check_email_not_available
from fastapi.responses import JSONResponse
from core.auth.oauth2 import get_current_user, is_admin, is_superuser
from core.parameters_check import is_strong_password, is_valid_email

# router = APIRouter(prefix='/user', tags=['user'])
router = APIRouter(prefix="/api/user")


# create user
@router.post("/signup", response_model=UserDisplay)
def create_user(user: UserBase):
    if check_username(user.username):
        return JSONResponse(status_code=406, content="username already exist ")
    elif check_email_not_available:
        return JSONResponse(status_code=406, content=" email already is available ")
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
@router.put("/edit-profile")
def update_user(user: UserUpdate, current_user: UserBase = Depends(get_current_user)):
    if user:
        if not is_valid_email(user.email):
            return JSONResponse(status_code=406, content="email is not valid ")

        elif check_email_not_available:
            return JSONResponse(status_code=500, content=" email already is available ")

        user_obj = UserCRUD()
        result = user_obj.update(user=user.dict(), userID=current_user["userID"])

        if result:
            return JSONResponse(status_code=200, content=result)
        else:
            return JSONResponse(status_code=400, content=" user not found ")


@router.patch("/block-user/{username}", dependencies=[Depends(is_admin)])
def block_user(username: str):
    user = UserCRUD()
    result = user.block_user(username)
    if result:
        return JSONResponse(status_code=200, content=result)

    else:
        return JSONResponse(status_code=400, content="username not found ")


@router.patch("/admin-access", dependencies=[Depends(is_superuser)])
def admin_access(username: str):
    user = UserCRUD()
    result = user.admin_access(username)
    if result:
        return JSONResponse(status_code=200, content=result)

    else:
        return JSONResponse(status_code=400, content="username not found ")
