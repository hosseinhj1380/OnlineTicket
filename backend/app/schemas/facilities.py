from pydantic import BaseModel


class Facilities(BaseModel):
    name: str


class FacilitiesUpdate(Facilities):
    new_name: str
