from pydantic import BaseModel

class Especialidades(BaseModel):
    codigo: str
    name: str
    resolucion: str

    class Config:
        orm_mode = True