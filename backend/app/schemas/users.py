from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    password: str
    full_name : str

class UserDisplay(BaseModel):
    username:str
    email:str
    full_name : str
    

