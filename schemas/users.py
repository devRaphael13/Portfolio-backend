from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    id: int
    image_url: str
    image_public_id: str
    resume_url: str
    resume_public_id: str

    model_config = {
        "from_attributes": True
    }

class UserCreate(BaseModel):
    image_url: str = Field(..., max_length=240)
    image_public_id: str = Field(..., max_length=120)
    resume_url: str = Field(..., max_length=240)
    resume_public_id: str = Field(..., max_length=120)

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    image_url: str = Field(None, max_length=240)
    image_public_id: str = Field(None, max_length=120)
    resume_url: str = Field(None, max_length=240)
    resume_public_id: str = Field(None, max_length=120)

    model_config = {
        "from_attributes": True
    }
