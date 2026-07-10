from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from sqlalchemy.orm import relationship
from database import Base
from models.associations import case_study_stack_association

class StackCategory(Enum):
    FRONTEND = "Frontend"
    BACKEND = "Backend"
    DATABASE = "Database"
    LANGUAGES = "Languages"
    INFRASTRUCTURE = "Infrastructure"

class Stack(Base):
    __tablename__ = "stack"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(SQLEnum(StackCategory), nullable=False)
    years = Column(Integer, nullable=False)
    case_studies = relationship("CaseStudy", secondary=case_study_stack_association, back_populates="stack")
