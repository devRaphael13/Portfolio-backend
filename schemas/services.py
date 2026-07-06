from pydantic import BaseModel, Field

class ServiceResponse(BaseModel):
    id: int
    icon_name: str
    name: str
    tagline: str
    features: list[str]

class ServiceCreate(BaseModel):
    icon_name: str
    name: str
    tagline: str
    features: list[str]

class ServiceUpdate(BaseModel):
    icon_name: str | None = None
    name: str | None = None
    tagline: str | None = None
    features: list[str] | None = None

    