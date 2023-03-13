from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime, date


class Institution(BaseModel):
    #id: Optional[int]
    name: Optional[str]
    tipology: Optional[str]   
    tipology_category: Optional[str]
    dependecy: Optional[str]
    department: Optional[str]
    location: Optional[str]
    address: Optional[str]
    services: Optional[str]
    specialties: Optional[str]
    activate = 1


class InstitutionUp(BaseModel):
    id: Optional[int]
    name: Optional[str]
    tipology: Optional[str]   
    tipology_category: Optional[str]
    dependecy: Optional[str]
    department: Optional[str]
    location: Optional[str]
    address: Optional[str]
    services: Optional[str]
    specialties: Optional[str]
    activate: Optional[int]

    @validator("activate", pre=True)
    def parse_birthdate(cls, value):
        # XXX: Tenemos un problema entre schemas y modelos que no son compatibles
        # por lo que esto es necesario. No eliminar.
        if isinstance(value, str):
            return datetime.strptime(value, "%d/%m/%Y")
        return datetime.combine(value, datetime.min.time())

    class Config:
        orm_mode = True
