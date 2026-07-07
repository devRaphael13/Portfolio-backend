from sqlalchemy import Column, Integer, String, Date
from database import Base

class Experiences(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(40), nullable=False)
    company = Column(String(40), nullable=False)
    url = Column(String(240), nullable=False)
    location = Column(String(20), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
