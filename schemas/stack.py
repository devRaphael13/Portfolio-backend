from pydantic import BaseModel, Field
from models.stack import StackCategory

class StackEdit(BaseModel):
    name: str
    category: StackCategory
    years: int

    model_config = {
        "from_attributes": True
    }

class StackResponse(BaseModel):
    id: int
    name: str
    category: StackCategory
    years: int

    model_config = {
        "from_attributes": True
    }

class StackCategoryGroup(BaseModel):
    category: StackCategory
    stacks: list[StackResponse] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }

class GroupedStackResponse(BaseModel):
    groups: list[StackCategoryGroup] = Field(default_factory=list)

    model_config = {
        "from_attributes": True
    }

