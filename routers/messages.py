from fastapi import Depends, HTTPException, APIRouter, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.messages import MessageCreate, MessageResponse
from models.messages import Message

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.post("/", response_model=MessageResponse, status_code=status.HTTP_201_CREATED)
def create_message(data: MessageCreate, db: Session = Depends(get_db)):
    message = Message(**data.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)

    return message

@router.get("/", response_model=Page[MessageResponse])
def list_message(db: Session = Depends(get_db)):
    case_studies = db.query(Message)
    return paginate(case_studies)

@router.get("/{message_id}", response_model=MessageResponse)
def retrieve_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()

    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    
    return message

@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(Message).filter(Message.id == message_id).first()

    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Message not found")
    
    db.delete(message)
    db.commit()

