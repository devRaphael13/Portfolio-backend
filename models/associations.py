from database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey

case_study_stack_association = Table(
    "case_study_stack",
    Base.metadata,
    Column("case_study_id", Integer, ForeignKey("case_studies.id"), primary_key=True),
    Column("stack_id", Integer, ForeignKey("stack.id"), primary_key=True)
)