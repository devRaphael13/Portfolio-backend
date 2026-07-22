from fastapi import Depends, APIRouter, status, Query, HTTPException
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.stack import StackEdit, StackResponse, StackCategoryGroup
from models.stack import Stack, StackCategory
from typing import Union
from collections import defaultdict

router = APIRouter(prefix="/stack", tags=["Stack"])

@router.post("/", response_model=StackResponse, status_code=status.HTTP_201_CREATED)
def create_stack(data: StackEdit, db: Session = Depends(get_db)):
    stat = Stack(**data.model_dump())
    db.add(stat)
    db.commit()
    db.refresh(stat)

    return stat

@router.get("/", response_model=Union[list[StackCategoryGroup], list[StackResponse]])
def list_stack(grouped: bool = Query(default=False), db: Session = Depends(get_db)):
    stacks = db.query(Stack).order_by(Stack.category).all()

    if not grouped:
        return stacks

    groups: dict[StackCategory, list[Stack]] = defaultdict(list)
    for s in stacks:
        groups[s.category].append(s)

    return [
        StackCategoryGroup(category=cat, stacks=groups[cat])
        for cat in StackCategory
    ]

@router.patch("/{stack_id}", response_model=StackResponse)
def update_stack(stack_id: int, data: StackEdit, db: Session = Depends(get_db)):
    stack = db.query(Stack).filter(Stack.id == stack_id).first()

    if not stack:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stack not found")
    
    for field, value in data.model_dump(exclude_none=True, exclude_unset=True).items():
        setattr(stack, field, value)

    db.commit()
    db.refresh(stack)

    return stack

@router.delete("/{stack_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stack(stack_id: int, db: Session = Depends(get_db)):
    stack = db.query(Stack).filter(Stack.id == stack_id).first()

    if not stack:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stack not found")
    
    db.delete(stack)
    db.commit()
