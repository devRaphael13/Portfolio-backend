from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    project_type = Column(String(40), nullable=False)
    company = Column(String(40), nullable=True)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

