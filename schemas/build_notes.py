from pydantic import BaseModel, Field
from datetime import datetime

class ParagraphResponse(BaseModel):
    id: int
    content: str
    order: int
    build_note_id: int

    model_config = {
        "from_attributes": True
    }

class ParagraphCreate(BaseModel):
    content: str
    order: int

    model_config = {
        "from_attributes": True
    }

class ParagraphOrder(BaseModel):
    id: int
    order: int

class ParagraphUpdate(BaseModel):
    id: int
    content: str = Field(min_length=1)

class BuildNotesResponse(BaseModel):
    id: int
    title: str
    tagline: str
    read_time: int
    created_at: datetime
    paragraphs: list[ParagraphResponse] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }

class BuildNotesLiteResponse(BaseModel):
    id: int
    title: str
    tagline: str
    read_time: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class BuildNotesCreate(BaseModel):
    title: str = Field(..., max_length=240)
    tagline: str = Field(..., max_length=240)
    read_time: int
    paragraphs: list[ParagraphCreate]

    model_config = {
        "from_attributes": True
    }

class BuildNotesUpdate(BaseModel):
    title: str | None = Field(None, max_length=240)
    tagline: str | None = Field(None, max_length=240)
    read_time: int | None = None

    model_config = {
        "from_attributes": True
    }
    