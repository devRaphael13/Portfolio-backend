from sqlalchemy import Column, Integer, String
from database import Base

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    image_public_id = Column(String, nullable=False)
    resume_url = Column(String, nullable=False)
    resume_public_id = Column(String, nullable=False)
    
