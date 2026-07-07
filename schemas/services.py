from pydantic import BaseModel, Field

class ServiceResponse(BaseModel):
    id: int
    icon_name: str 
    name: str
    tagline: str
    features: list[str]

class ServiceCreate(BaseModel):
    icon_name: str = Field(..., max_length=40)
    name: str = Field(..., max_length=40)
    tagline: str = Field(..., max_length=240)
    features: list[str]

class ServiceUpdate(BaseModel):
    icon_name: str | None = Field(None, max_length=40)
    name: str | None = Field(None, max_length=40)
    tagline: str | None = Field(None, max_length=240)
    features: list[str] | None = None

    