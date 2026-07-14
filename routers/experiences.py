from fastapi import Depends, HTTPException, APIRouter, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.experiences import ExperienceCreate, ExperienceResponse, ExperienceUpdate
from models.experiences import Experience

router = APIRouter(prefix="/experiences", tags=["Experiences"])

@router.post("/", response_model=ExperienceResponse, status_code=status.HTTP_201_CREATED)
def create_experience(data: ExperienceCreate, db: Session = Depends(get_db)):
    experience = Experience(**data.model_dump())
    db.add(experience)
    db.commit()
    db.refresh(experience)

    return experience

@router.get("/", response_model=Page[ExperienceResponse])
def list_experience(db: Session = Depends(get_db)):
    experience = db.query(Experience)
    return paginate(experience)

@router.get("/{experience_id}", response_model=ExperienceResponse)
def retrieve_experience(experience_id: int, db: Session = Depends(get_db)):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()

    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")
    
    return experience

@router.patch("/{experience_id}", response_model=ExperienceResponse)
def update_experience(experience_id: int, data: ExperienceUpdate, db: Session = Depends(get_db)):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()

    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")
    
    for field, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(experience, field, value)

    db.commit()
    db.refresh(experience)

    return experience

@router.delete("/{experience_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_experience(experience_id: int, db: Session = Depends(get_db)):
    experience = db.query(Experience).filter(Experience.id == experience_id).first()

    if not experience:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Experience not found")
    
    db.delete(experience)
    db.commit()

