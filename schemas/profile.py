from pydantic import BaseModel, Field

class ProfileResponse(BaseModel):
    id: int
    image_url: str
    image_public_id: str
    resume_url: str
    resume_public_id: str

    model_config = {
        "from_attributes": True
    }

class ProfileUpdate(BaseModel):
    image_url: str | None = None
    image_public_id: str | None = None
    resume_url: str | None = None
    resume_public_id: str | None = None

    model_config = {
        "from_attributes": True
    }
