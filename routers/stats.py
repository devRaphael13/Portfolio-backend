from fastapi import Depends, HTTPException, APIRouter, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.stats import StatCreate, StatResponse, StatUpdate
from models.stats import Stat

router = APIRouter(prefix="/stats", tags=["Stats"])

@router.post("/", response_model=StatResponse, status_code=status.HTTP_201_CREATED)
def create_stat(data: StatCreate, db: Session = Depends(get_db)):
    stat = Stat(**data.model_dump())
    db.add(stat)
    db.commit()
    db.refresh(stat)

    return stat

@router.get("/", response_model=Page[StatResponse])
def list_stat(db: Session = Depends(get_db)):
    stats = db.query(Stat)
    return paginate(stats)

@router.get("/{stat_id}", response_model=StatResponse)
def retrieve_stat(stat_id: int, db: Session = Depends(get_db)):
    stat = db.query(Stat).filter(Stat.id == stat_id).first()

    if not stat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stat not found")
    
    return stat

@router.patch("/{stat_id}", response_model=StatResponse)
def update_stat(stat_id: int, data: StatUpdate, db: Session = Depends(get_db)):
    stat = db.query(Stat).filter(Stat.id == stat_id).first()

    if not stat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stat not found")
    
    for field, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(stat, field, value)

    db.commit()
    db.refresh(stat)

    return stat

@router.delete("/{stat_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_stat(stat_id: int, db: Session = Depends(get_db)):
    stat = db.query(Stat).filter(Stat.id == stat_id).first()

    if not stat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Stat not found")
    
    db.delete(stat)
    db.commit()

