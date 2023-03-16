from typing import Optional
from pydantic import BaseModel


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

    
