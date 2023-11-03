from fastapi import APIRouter, Depends, status

from fastapi.exceptions import HTTPException 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from crud.users_crud import authenticate_user
from core.hash import Hash

from . import oauth2


router = APIRouter()



@router.post("/api/oauth2/login")
def get_token(request: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(request.username )
    

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid credential"
        )

    if not Hash.verify(user.get("password"), request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid password"
        )

    access_token = oauth2.create_access_token(data={"sub": request.username})

    return {
        "access_token": access_token,
        "type_token": "bearer",
        "username": user.get("username"),
    }
