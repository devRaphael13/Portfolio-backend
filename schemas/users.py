from pydantic import BaseModel, Field, EmailStr

class UserResponse(BaseModel):
    id: int
    email: str
    image_url: str | None
    image_public_id: str | None
    resume_url: str | None
    resume_public_id: str | None

    model_config = {
        "from_attributes": True
    }

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., max_length=255)
    image_url: str | None = Field(None, max_length=240)
    image_public_id: str | None = Field(None, max_length=120)
    resume_url: str | None = Field(None, max_length=240)
    resume_public_id: str | None = Field(None, max_length=120)

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    email: EmailStr | None = Field(None, max_length=40)
    password: str | None = Field(None, max_length=255)
    image_url: str | None = Field(None, max_length=240)
    image_public_id: str | None = Field(None, max_length=120)
    resume_url: str | None = Field(None, max_length=240)
    resume_public_id: str | None = Field(None, max_length=120)

    model_config = {
        "from_attributes": True
    }
