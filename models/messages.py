from sqlalchemy import Column, Integer, String, Text, DateTime, Enum
from database import Base

class ProjectTypeEnum(Enum):
    FULL_STACK_DEVELOPMENT = "Full Stack Development"
    FRONT_END_DEVELOPMENT = "Front End Development"
    BACKEND_DEVELOPMENT = "Back End Development"
    DEVOPS = "DevOps"
    NOT_SURE = "Not Sure"


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    project_type = Column(Enum(ProjectTypeEnum), nullable=False)
    company = Column(String, nullable=True)
    message = Column(Text, nullable=False)

