from pydantic import BaseModel

class CreateComment(BaseModel):
    text:str
    thread:int

class UpdateComment(BaseModel):
    text:str
    