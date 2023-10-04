from pydantic import BaseModel

class Services(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True