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
    role: str
    company: str
    url: str
    location: str
    start_date: date
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

class ExperienceUpdate(BaseModel):
    role: str | None = None
    company: str | None = None
    url: str | None = None
    location: str | None = None
    start_date: date | None = None
    end_date: date | None = None

    model_config = {
        "from_attributes": True
    }

    