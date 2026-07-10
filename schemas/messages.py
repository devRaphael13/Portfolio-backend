from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class MessageResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    project_type: str
    company: str | None = None
    message: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class MessageCreate(BaseModel):
    full_name: str = Field(..., max_length=40)
    email: EmailStr
    project_type: str = Field(..., max_length=40)
    company: str | None = Field(None, max_length=40)
    message: str

    model_config = {
        "from_attributes": True
    }

