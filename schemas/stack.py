from pydantic import BaseModel, Field

class StackCreate(BaseModel):
    name: str
    category: str = Field(..., max_length=20)
    years: int

    model_config = {
        "from_attributes": True
    }

class StackUpdate(BaseModel):
    name: str | None = None
    category: str | None = Field(None, max_length=20)
    years: int | None = None

    model_config = {
        "from_attributes": True
    }

class StackResponse(BaseModel):
    id: int
    name: str
    category: str
    years: int

    model_config = {
        "from_attributes": True
    }

class StackCategoryGroup(BaseModel):
    category: str
    stacks: list[StackResponse] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }

class GroupedStackResponse(BaseModel):
    groups: list[StackCategoryGroup] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }

