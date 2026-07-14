from fastapi import APIRouter, Depends, status, Query, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session, joinedload
from dependencies.db import get_db
from schemas.build_notes import BuildNotesCreate, BuildNotesResponse, BuildNotesUpdate, BuildNotesLiteResponse
from models.build_notes import BuildNote, Paragraph

router = APIRouter(prefix="/notes", tags=["Build Notes"])

@router.post("/", response_model=BuildNotesResponse, status_code=status.HTTP_201_CREATED)
def create_note(data: BuildNotesCreate, db: Session = Depends(get_db)):
    paragraph_models = [Paragraph(order=i.order, content=i.content) for i in data.paragraphs]

    note = BuildNote(
        title=data.title,
        tagline=data.tagline,
        read_time=data.read_time,
        paragraphs=paragraph_models
    )

    db.add(note)
    db.commit()
    db.refresh(note)

    return note


@router.get("/", response_model=Page[BuildNotesLiteResponse])
def list_notes(db: Session = Depends(get_db)):
    notes = db.query(BuildNote)
    return paginate(notes)

@router.get("/{note_id}", response_model=BuildNotesResponse)
def retrieve_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(BuildNote).options(
        joinedload(BuildNote.paragraphs)
    ).filter(BuildNote.id == note_id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    return note

@router.patch("/{note_id}", response_model=BuildNotesResponse)
def update_note(note_id: int, data: BuildNotesUpdate, db: Session = Depends(get_db)):
    note = db.query(BuildNote).filter(BuildNote.id == note_id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    
    for field, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(note, field, value)
    
    db.commit()
    db.refresh(note)

    note = db.query(BuildNote).options(
        joinedload(BuildNote.paragraphs)
    ).filter(BuildNote.id == note_id)

    return note

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(BuildNote).filter(BuildNote.id == note_id).first()

    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")
    
    db.delete(note)
    db.commit()


