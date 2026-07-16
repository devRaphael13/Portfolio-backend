from pydantic import BaseModel, Field
from datetime import date
from schemas.stack import StackResponse

class ExperienceName(BaseModel):
    id: int
    company: str

    model_config = {
        "from_attributes": True
    }

class CaseStudyResponse(BaseModel):
    id: int
    industry: str
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
    experience: ExperienceName | None = None

    model_config = {
        "from_attributes": True
    }


class CaseStudyCreate(BaseModel):
    industry: str = Field(..., max_length=40)
    title: str = Field(..., max_length=120)
    url: str = Field(..., max_length=240)
    image_url: str = Field(..., max_length=240)
    image_public_id: str = Field(..., max_length=120)
    problem: str
    solution: str
    stack_ids: list[int] = Field(default_factory=list)
    featured: bool = Field(default=False)
    experience_id: int | None = Field(default=None)
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class CaseStudyUpdate(BaseModel):
    industry: str | None = Field(None, max_length=40)
    title: str | None = Field(None, max_length=120)
    url: str | None = Field(None, max_length=240)
    image_url: str | None = Field(None, max_length=240)
    image_public_id: str | None = Field(None, max_length=120)
    featured: bool | None = Field(None)
    experience_id: int | None = Field(default=None)
    problem: str | None = None
    solution: str | None = None
    start_date: date | None = None
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class StackUpdate(BaseModel):
    stack_ids: list[int]

    model_config = {
        "from_attributes": True
    }
