from pydantic import BaseModel
from typing import List
from datetime import date
class Person(BaseModel):
    full_name:str
    profile_photo:str
    birthdate:str
    images:List[str]
    social_medias:List[dict]=[{"instagram":"",
                                "twitter":""}]
    biography:str
    birthplace:dict={"name_fa": "",
                     "name_en": ""}
    roles:List[dict]=[{"id":0,
                       "name":"string"}]
    
class PersonRole(BaseModel):
    
    name:str