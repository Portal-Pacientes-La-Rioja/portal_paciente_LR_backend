from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.config.database import Base


class StudyType(Base):
    __tablename__ = "study_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(100), nullable=False)

    studies = relationship("Studies", back_populates="study_type")

    def __init__(self, type_name: str):
        self.type_name = type_name
