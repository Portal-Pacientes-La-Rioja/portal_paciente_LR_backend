from sqlalchemy import Column, Integer, String

from app.config.database import Base

class Institutions(Base):

    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    tipology = Column(String(100), nullable=False)
    tipology_category = Column(String(100), nullable=False)
    dependecy = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    location = Column(String(100), nullable=False)
    address = Column(String(100), nullable=False)
    services = Column(String(100), nullable=False)
    specialties = Column(String(100), nullable=False)
    activate = Column(Integer)

    def __init__(self, id: int,name: str, tipology: str, tipology_category: str, dependecy: str,
                 department: str, location: str, address: str, services: str, specialties: str,
                 activate: int
                 ):
                 
        
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

