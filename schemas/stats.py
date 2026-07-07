from pydantic import BaseModel, Field

class StatResponse(BaseModel):
    id: int
    name: str
    value: int

class StatCreate(BaseModel):
    name: str = Field(..., max_length=120)
    value: int

class StatUpdate(BaseModel):
    name: str | None = Field(None, max_length=120)
    value: int | None = None
