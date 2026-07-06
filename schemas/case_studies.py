from pydantic import BaseModel, Field
from datetime import date
from schemas.stack import StackResponse

class CaseStudyResponse(BaseModel):
    id: int
    product_type: str
    title: str
    problem: str
    solution: str
    stack: list[StackResponse] = Field(default_factory=list)
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class CaseStudyCreate(BaseModel):
    product_type: str
    title: str
    problem: str
    solution: str
    stack_ids: list[int] = Field(default_factory=list)
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class CaseStudyUpdate(BaseModel):
    product_type: str | None = None
    title: str | None = None
    problem: str | None = None
    solution: str | None = None
    stack_ids: list[int] | None = None
    start_date: date | None = None
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }
