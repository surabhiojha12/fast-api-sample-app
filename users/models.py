from sqlalchemy import Column, ForeignKey, Integer, String

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    ph_no = Column(String)
