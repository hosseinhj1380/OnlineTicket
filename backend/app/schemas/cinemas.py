from pydantic import BaseModel 
from typing import List


class Cinema(BaseModel):
    name : str 
    address : str
    images : List[str]
    website : str
    description :str
    location : dict = {"lat": "35.75545120239258", "long": " 51.19039154052734"}
    facility : List[str]    
    telephones : List[str] = ["021-12345678"]
    established_at : str
    rules : List[str]
    city : int
    
class Halls(BaseModel):
    name : str
    capacity : int 
    min_price : int
    max_price : int
    

class Session(BaseModel):
    movieID :int
    start_at : str ="21:55:00+03:30"
    start_release_date : str =  "2023-11-16T21:55:00+03:30"
    end_release_date : str = "2023-11-16T21:55:00+03:30"
    
class UpdateSession(Session):
    sessionID :int
