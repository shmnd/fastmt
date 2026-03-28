from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import CreateUser, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_description=UserResponse)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list    [UserResponse])
def list_user(db: Session = Depends(get_db)):
    return db.query(User).all()






