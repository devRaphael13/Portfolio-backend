from fastapi import Depends, HTTPException, APIRouter, status
from dependencies.db import get_db
from sqlalchemy.orm import Session
from schemas.users import UserCreate, UserResponse, UserUpdate
from models.users import User
import bcrypt


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
    user = User(
        email=data.email,
        hashed_password=hashed.decode()
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get("/{user_id}", response_model=UserResponse)
def retrieve_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user

@router.patch("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    for field, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        if field == "password":
            hashed = bcrypt.hashpw(value.encode(), bcrypt.gensalt())
            field = "hashed_password"
            value = hashed.decode()

        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    return user
