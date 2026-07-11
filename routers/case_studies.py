from fastapi import Depends, HTTPException, APIRouter, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.case_studies import CaseStudyCreate, CaseStudyResponse, CaseStudyUpdate
from models.case_studies import CaseStudy

router = APIRouter(prefix="/case-studies", tags=["Case Studies"])

@router.post("/", response_model=CaseStudyResponse, status_code=status.HTTP_201_CREATED)
def create_case_study(data: CaseStudyCreate, db: Session = Depends(get_db)):
    case_study = CaseStudy(**data.model_dump())
    db.add(case_study)
    db.commit()
    db.refresh(case_study)

    return case_study

@router.get("/", response_model=Page[CaseStudyResponse])
def list_case_study(db: Session = Depends(get_db)):
    case_studies = db.query(CaseStudy)
    return paginate(case_studies)

@router.get("/{case_study_id}", response_model=CaseStudyResponse)
def retrieve_case_study(case_study_id: int, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case Study not found")
    
    return case_study

@router.patch("/{case_study_id}", response_model=CaseStudyResponse)
def update_case_study(case_study_id: int, data: CaseStudyUpdate, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case Study not found")
    
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(case_study, field, value)

    db.commit()
    db.refresh(case_study)

    return case_study

@router.delete("/{case_study_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_case_study(case_study_id: int, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case Study not found")
    
    db.delete(case_study)
    db.commit()

