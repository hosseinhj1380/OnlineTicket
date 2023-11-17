from pydantic import BaseModel 
from typing import List


class Cinema(BaseModel):
    name : str 
    address : str
    images : List[str]
    website : str
    description :str
    # location : str 
    facility : List[str]    
    telephones : List[str]
    established_at : str
    rules : List[str]
    city : int
    
    
    