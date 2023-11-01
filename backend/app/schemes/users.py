from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    password: str

class UserDisplay(BaseModel):
    username:str
    email:str

    