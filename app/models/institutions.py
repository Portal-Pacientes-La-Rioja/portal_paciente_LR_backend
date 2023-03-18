from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class Institutions(Base):

    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    codigo = Column(String(100), nullable=False)
    domicilio = Column(String(100), nullable=False)
    lat = Column(String(20), nullable=False)
    long = Column(String(20), nullable=False)
    tipologia = Column(String(100), nullable=False)
    categoria_tipologia = Column(String(100), nullable=False)
    dependencia = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=False)
    localidad = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    activate = Column(Integer, default=1)

    services = relationship("Services", secondary="institutions_services", back_populates="institutions")
    especialidades = relationship("Especialidades",
                                  secondary="institutions_especialidades",
                                  back_populates="institutions")

    def __init__(self, id: int, name: str, tipology: str, tipology_category: str, dependecy: str,
                 department: str, location: str, address: str, services: str, specialties: str,
                 activate: int):
        self.id = id
        self.name = name        
        self.tipology = tipology
        self.tipology_category = tipology_category
        self.dependecy = dependecy
        self.department = department
        self.location = location
        self.address = address
        self.services = services
        self.specialties = specialties
        self.activate = activate
