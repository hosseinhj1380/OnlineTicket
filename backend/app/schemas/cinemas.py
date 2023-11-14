from pydantic import BaseModel 
from typing import List


class Cinema(BaseModel):
    name : str 
    address : str
    images : List[str]
    website : str
     