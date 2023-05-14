from typing import Dict

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from app.config.database import Base


class Institutions(Base):
    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    codigo = Column(String(100), nullable=False)
    domicilio = Column(String(500), nullable=False)
    lat = Column(Float, nullable=True)
    long = Column(Float, nullable=True)
    tipologia = Column(String(100), nullable=False)
    categoria_tipologia = Column(String(100), nullable=False)
    dependencia = Column(String(100), nullable=False)
    departamento = Column(String(100), nullable=False)
    localidad = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    activate = Column(Integer, default=1)
    telefono = Column(Integer, default=0)

    services = relationship("Services", secondary="institutions_services", back_populates="institutions")
    especialidades = relationship("Especialidades",
                                  secondary="institutions_especialidades",
                                  back_populates="institutions")
    user = relationship("User", secondary="institutions_user", back_populates="institutions")

    def as_dict(self) -> Dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != "id"}
