from typing import Optional

from pydantic import BaseModel


# TODO: Add relationship between services and specialities
class Institution(BaseModel):
    name: str
    code: str
    address: str
    lat: Optional[float]
    long: Optional[float]
    tipology: str
    tipology_category: str
    dependecy: str
    department: str
    location: str
    city: str
    activate = 1


class InstitutionUp(BaseModel):
    name: Optional[str]
    code: Optional[str]
    address: Optional[str]
    lat: Optional[float]
    long: Optional[float]
    tipology: Optional[str]   
    tipology_category: Optional[str]
    dependecy: Optional[str]
    department: Optional[str]
    location: Optional[str]
    city: Optional[str]
    activate: Optional[int]
    # services: Optional[str]
    # specialties: Optional[str]

    class Config:
        orm_mode = True
