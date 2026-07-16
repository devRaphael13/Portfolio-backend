from fastapi import Depends, HTTPException, APIRouter, status, Query
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.db import get_db
from sqlalchemy.orm import Session, joinedload, selectinload
from schemas.case_studies import CaseStudyCreate, CaseStudyResponse, CaseStudyUpdate, StackUpdate
from schemas.stack import StackResponse
from models.case_studies import CaseStudy
from models.stack import Stack
from models.experiences import Experience
from typing import Optional


router = APIRouter(prefix="/case-studies", tags=["Case Studies"])

@router.post("/", response_model=CaseStudyResponse, status_code=status.HTTP_201_CREATED)
def create_case_study(data: CaseStudyCreate, db: Session = Depends(get_db)):
    payload = data.model_dump(exclude={"stack_ids"})
    case_study = CaseStudy(**payload)

    if data.experience_id is not None:
        experience = db.query(Experience).filter(Experience.id == data.experience_id).first()
        if not experience:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Experience id {data.experience_id} not found"
            )

    if data.stack_ids:
        stacks = db.query(Stack).filter(Stack.id.in_(data.stack_ids)).all()
        found_ids = {s.id for s in stacks}
        missing = set(data.stack_ids) - found_ids
        if missing:
            raise HTTPException(status_code=400, detail=f"Stack ids not found: {sorted(missing)}")
        case_study.stack = stacks

    db.add(case_study)
    db.commit()
    db.refresh(case_study)
    return case_study

@router.get("/", response_model=Page[CaseStudyResponse])
def list_case_study(featured: Optional[bool] = Query(default=None), db: Session = Depends(get_db)):
    case_studies = db.query(CaseStudy).options(
        joinedload(CaseStudy.experience),
        selectinload(CaseStudy.stack)
        )

    if featured is not None:
        case_studies = case_studies.filter(CaseStudy.featured == featured)
    return paginate(case_studies)

@router.get("/{case_study_id}", response_model=CaseStudyResponse)
def retrieve_case_study(case_study_id: int, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).options(
        joinedload(CaseStudy.experience),
        selectinload(CaseStudy.stack)
    ).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case Study not found")
    
    return case_study

@router.patch("/{case_study_id}", response_model=CaseStudyResponse)
def update_case_study(case_study_id: int, data: CaseStudyUpdate, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case Study not found")
    
    for field, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(case_study, field, value)

    db.commit()
    db.refresh(case_study)

    return case_study

@router.post("/{case_study_id}/add_stack", response_model=list[StackResponse])
def add_stack(case_study_id: int, data: StackUpdate, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).options(
        selectinload(CaseStudy.stack)
    ).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case study not found")

    stacks = db.query(Stack).filter(Stack.id.in_(data.stack_ids)).all()
    found_ids = {s.id for s in stacks}
    missing = set(data.stack_ids) - found_ids
    if missing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Stack ids not found: {sorted(missing)}")

    existing_ids = {s.id for s in case_study.stack}
    for stack in stacks:
        if stack.id not in existing_ids:
            case_study.stack.append(stack)

    db.commit()
    db.refresh(case_study)
    return case_study.stack


@router.post("/{case_study_id}/remove_stack", response_model=list[StackResponse])
def remove_stack(case_study_id: int, data: StackUpdate, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).options(
        selectinload(CaseStudy.stack)
    ).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case study not found")

    ids_to_remove = set(data.stack_ids)
    case_study.stack = [s for s in case_study.stack if s.id not in ids_to_remove]

    db.commit()
    db.refresh(case_study)
    return case_study.stack

@router.delete("/{case_study_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_case_study(case_study_id: int, db: Session = Depends(get_db)):
    case_study = db.query(CaseStudy).filter(CaseStudy.id == case_study_id).first()

    if not case_study:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case Study not found")
    
    db.delete(case_study)
    db.commit()

