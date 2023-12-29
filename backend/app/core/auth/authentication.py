from fastapi import APIRouter, Depends, status

from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from crud.users_crud import authenticate_user
from core.hash import Hash
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
import requests
from jose import jwt

from . import oauth2


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Replace these with your own values from the Google Developer Console
GOOGLE_CLIENT_ID = ""
GOOGLE_CLIENT_SECRET = ""
GOOGLE_REDIRECT_URI = "http://127.0.0.1:8000/"

@router.get("/login/google")
def login_google():
    return {
        "url": f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20profile%20email&access_type=offline"
    }

@router.get("/")
def auth_google(code: str):
    token_url = "https://accounts.google.com/o/oauth2/token"
    
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }
    response = requests.post(token_url, data=data)
    access_token = response.json().get("access_token")
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo", headers={"Authorization": f"Bearer {access_token}"})
    print(user_info.json())
    return user_info.json()

@router.get("/google/token")
async def get_token(token: str = Depends(oauth2_scheme)):
    return jwt.decode(token, GOOGLE_CLIENT_SECRET, algorithms=["HS256"])


@router.post("/api/oauth2/login")
def get_token(request: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(request.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid credential"
        )

    if not Hash.verify(user.get("password"), request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="invalid password"
        )
    if user["state"] == "block":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=" your user has been blocked "
        )

    access_token = oauth2.create_access_token(data={"sub": request.username})

    return {
        "access_token": access_token,
        "type_token": "bearer",
        "username": user.get("username"),
    }
