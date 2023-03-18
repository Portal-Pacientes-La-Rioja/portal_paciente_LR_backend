from sqlalchemy import Column, Integer, ForeignKey

from app.config.database import Base


class InstitutionsEspecialidades(Base):
    __tablename__ = "institutions_especialidades"

    institutions_id = Column(Integer, ForeignKey('institutions.id'), primary_key=True)
    especialidades_id = Column(Integer, ForeignKey('especialidades.id'), primary_key=True)
