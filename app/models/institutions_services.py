from sqlalchemy import Column, Integer, ForeignKey

from app.config.database import Base


class InstitutionsServices(Base):
    __tablename__ = "institutions_services"

    institutions_id = Column(Integer, ForeignKey('institutions.id'), primary_key=True)
    services_id = Column(Integer, ForeignKey('services.id'), primary_key=True)
