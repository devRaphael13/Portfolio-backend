from pydantic import BaseModel, Field
from datetime import date
from schemas.stack import StackResponse

class CaseStudyResponse(BaseModel):
    id: int
    product_type: str
    title: str
    url: str
    image_url: str
    image_public_id: str
    problem: str
    solution: str
    stack: list[StackResponse] = Field(default_factory=list)
    featured: bool
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class CaseStudyCreate(BaseModel):
    product_type: str = Field(..., max_length=40)
    title: str = Field(..., max_length=120)
    url: str = Field(..., max_length=240)
    image_url: str = Field(..., max_length=240)
    image_public_id: str = Field(..., max_length=120)
    problem: str
    solution: str
    stack_ids: list[int] = Field(default_factory=list)
    featured: bool = Field(default=False)
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class CaseStudyUpdate(BaseModel):
    product_type: str | None = Field(None, max_length=40)
    title: str | None = Field(None, max_length=120)
    url: str = Field(None, max_length=240)
    image_url: str = Field(None, max_length=240)
    image_public_id: str = Field(None, max_length=120)
    featured: bool | None = Field(None)
    problem: str | None = None
    solution: str | None = None
    stack_ids: list[int] | None = None
    start_date: date | None = None
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }
