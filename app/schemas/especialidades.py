from pydantic import BaseModel

class Especialidades(BaseModel):
    id: int
    codigo: str
    name: str
    resolucion: str

    class Config:
        orm_mode = True