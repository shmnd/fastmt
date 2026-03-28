from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import CreateUser, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_data = user.dict()

    password = user_data.pop("password")
    hashed_password = f"{password}notsecure"

    db_user = User(**user_data, password=hashed_password)


    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=list[UserResponse])
def list_user(db: Session = Depends(get_db)):
    return db.query(User).all()






