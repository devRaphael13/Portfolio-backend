from sqlalchemy import Column, Integer, String, Text, Date, Boolean
from sqlalchemy.orm import relationship
from database import Base
from models.associations import case_study_stack_association

class CaseStudy(Base):
    __tablename__ = "case_studies"

    id = Column(Integer, primary_key=True, index=True)
    product_type = Column(String(40), nullable=False)
    url = Column(String(240), nullable=True)
    image_url = Column(String(240), nullable=False)
    image_public_id = Column(String(120), nullable=False)
    title = Column(String(120), nullable=False)
    problem = Column(Text, nullable=False)
    solution = Column(Text, nullable=False)
    featured = Column(Boolean, default=False)
    stack = relationship("Stack", secondary=case_study_stack_association, back_populates="case_studies")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    
