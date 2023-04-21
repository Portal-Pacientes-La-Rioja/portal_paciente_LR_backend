from sqlalchemy import Column, Integer, ForeignKey, BigInteger

from app.config.database import Base


class InstitutionsAdmin(Base):
    __tablename__ = "institutions_user"

    institutions_id = Column(Integer, ForeignKey('institutions.id'), primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.id'), primary_key=True)
