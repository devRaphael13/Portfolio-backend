from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from dependencies.db import get_db
from dependencies.auth import create_access_token
from models.users import User
from schemas.users import UserCreate, UserResponse
import bcrypt

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/sign-up", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def sign_up(data: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    
    hashed_byte = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())

    user = User(
        email=data.email,
        hashed_password=hashed_byte.decode()
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form.username).first()
    
    if not user or not bcrypt.checkpw(form.password.encode(), user.hashed_password.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}



