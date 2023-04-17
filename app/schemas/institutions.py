from typing import Optional, List, Union
from sqlalchemy.orm.collections import InstrumentedList

from pydantic import BaseModel


class Services(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Especialidades(BaseModel):
    id: int
    codigo: str
    name: str
    resolucion: str

    class Config:
        orm_mode = True


class Institution(BaseModel):
    id: int
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

    services: Union[List[int], List[Services]] = []
    especialidades: Union[List[int], List[Especialidades]] = []

    class Config:
        orm_mode = True


class InstitutionWithID(Institution):
    id: int
