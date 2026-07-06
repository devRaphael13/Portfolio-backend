from pydantic import BaseModel, Field

class StatResponse(BaseModel):
    id: int
    name: str
    value: int

class StatCreate(BaseModel):
    name: str
    value: int

class StatUpdate(BaseModel):
    name: str | None = None
    value: int | None = None
