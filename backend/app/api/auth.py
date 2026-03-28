from fastapi import APIRouter,Depends,HTTPException
from app.core.security import create_access_token,varify_password
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginSchema(BaseModel):
    email:str
    password:str

@router.post("/login")
def login(user:LoginSchema, db: Session=Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not varify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentails")
    
    token = create_access_token({"user_id":db_user.id})
    return {"access_token":token, "token_type":"bearer"}
    
