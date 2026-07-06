from pydantic import BaseModel, Field

class ParagraphResponse(BaseModel):
    id: int
    content: str
    order: int
    build_note_id: int

    model_config = {
        "from_attributes": True
    }

class BuildNotesResponse(BaseModel):
    id: int
    title: str
    tagline: str
    read_time: int
    created_at: str
    paragraphs: list[ParagraphResponse] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }

class BuildNotesCreate(BaseModel):
    title: str
    tagline: str
    read_time: int

    model_config = {
        "from_attributes": True
    }

class BuildNotesUpdate(BaseModel):
    title: str | None = None
    tagline: str | None = None
    read_time: int | None = None

    model_config = {
        "from_attributes": True
    }
