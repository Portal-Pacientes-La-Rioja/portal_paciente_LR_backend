from typing import Optional

from pydantic import BaseModel


# TODO: Add relationship between services and specialities
class Institution(BaseModel):
    name: str
    codigo: str
    domicilio: str
    lat: Optional[float]
    long: Optional[float]
    tipologia: str
    categoria_tipologia: str
    dependencia: str
    departamento: str
    localidad: str
    ciudad: str
    activate: int

    class Config:
        orm_mode = True


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
