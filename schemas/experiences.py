from pydantic import BaseModel, Field
from datetime import date

class ExperienceResponse(BaseModel):
    id: int
    role: str
    company: str
    url: str
    location: str
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class ExperienceCreate(BaseModel):
    role: str = Field(..., max_length=40) 
    company: str = Field(..., max_length=40)
    url: str = Field(..., max_length=240)
    location: str = Field(..., max_length=20)
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class ExperienceUpdate(BaseModel):
    role: str | None = Field(None, max_length=40)
    company: str | None = Field(None, max_length=40)
    url: str | None = Field(None, max_length=240)
    location: str | None = Field(None, max_length=20)
    start_date: date | None = None
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

    