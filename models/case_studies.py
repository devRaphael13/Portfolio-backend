from sqlalchemy import Column, Integer, String, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from database import Base
from models.associations import case_study_stack_association

class CaseStudy(Base):
    __tablename__ = "case_studies"

    id = Column(Integer, primary_key=True, index=True)
    product_type = Column(String, nullable=False)
    title = Column(String, nullable=False)
    problem = Column(Text, nullable=False)
    solution = Column(Text, nullable=False)
    stack = relationship("Stack", secondary=case_study_stack_association, back_populates="case_studies")
