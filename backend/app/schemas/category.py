from pydantic import BaseModel

class Category(BaseModel):
    name:str
    

class CategoryUpdate(Category):
    new_name :str
    