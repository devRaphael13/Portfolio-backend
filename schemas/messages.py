from pydantic import BaseModel, Field, EmailStr

class MessageResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    project_type: str
    company: str | None = None
    message: str
    created_at: str

    model_config = {
        "from_attributes": True
    }

class MessageCreate(BaseModel):
    full_name: str
    email: str
    project_type: str
    company: str | None = None
    message: str

    model_config = {
        "from_attributes": True
    }

