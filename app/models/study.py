from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, func
from sqlalchemy.orm import relationship

from app.config.database import Base


class Studies(Base):
    __tablename__ = "studies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_person = Column(Integer, ForeignKey('person.id'), nullable=True)
    id_study_type = Column(Integer, ForeignKey('study_type.id'), nullable=False)
    study_name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    file_path = Column(String(255), nullable=True)
    upload_date = Column(DateTime, default=func.now(), nullable=False)

    person = relationship("Person", back_populates="studies")
    study_type = relationship("StudyType", back_populates="studies")

    def __init__(self, id_person: int, id_study_type: int, study_name: str, description: str, file_path: str):
        self.id_person = id_person
        self.id_study_type = id_study_type
        self.study_name = study_name
        self.description = description
        self.file_path = file_path
