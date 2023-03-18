from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base


class Especialidades(Base):
    __tablename__ = "especialidades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    resolucion = Column(String(100), nullable=False)

    institutions = relationship("Institutions",
                                secondary="institutions_especialidades",
                                back_populates="especialidades")