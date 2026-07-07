from sqlalchemy import Column, Integer, String
from database import Base

class Stat(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    value = Column(Integer, nullable=False)