from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

from crud.users_crud import find_user



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/oauth2/login")

SECRET_KEY = "6c7d438d2ea66cc11ee315566bda6f45336930dc2a40eaa96ec009524c20aa69"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# data = {"sub" : username}
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def get_current_user(token: str=Depends(oauth2_scheme)):
  
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail='invalid credentials',
                                    headers={'WWW-authenticate': 'bearer'})

    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')
        if not username:
            raise error_credential
    except JWTError:
        raise error_credential

    user = find_user(username )

    return user


def is_admin(current_user: dict = Depends(get_current_user)):
    if "admin" in current_user.get("roles", []):
        return True
    raise HTTPException(status_code=403, detail="You do not have access to this resource")

def is_superuser(current_user: dict = Depends(get_current_user)):
    if "superuser" in current_user.get("roles", []):
        return True
    raise HTTPException(status_code=403, detail="You do not have access to this resource")