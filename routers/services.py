from fastapi import Depends, HTTPException, APIRouter, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.services import ServiceCreate, ServiceResponse, ServiceUpdate
from models.services import Service

router = APIRouter(prefix="/services", tags=["Services"])

@router.post("/", response_model=ServiceResponse, status_code=status.HTTP_201_CREATED)
def create_service(data: ServiceCreate, db: Session = Depends(get_db)):
    service = Service(**data.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)

    return service

@router.get("/", response_model=Page[ServiceResponse])
def list_service(db: Session = Depends(get_db)):
    services = db.query(Service)
    return paginate(services)

@router.get("/{service_id}", response_model=ServiceResponse)
def retrieve_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    
    return service

@router.patch("/{service_id}", response_model=ServiceResponse)
def update_service(service_id: int, data: ServiceUpdate, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(service, field, value)

    db.commit()
    db.refresh(service)

    return service

@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service not found")
    
    db.delete(service)
    db.commit()

