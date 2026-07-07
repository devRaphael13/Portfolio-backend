from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    image_url = Column(String(240), nullable=False)
    image_public_id = Column(String(120), nullable=False)
    resume_url = Column(String(240), nullable=False)
    resume_public_id = Column(String(120), nullable=False)
    
