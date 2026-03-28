from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.db.database import get_db
from app.schemas.task import CreateTask, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
def create_task(task: CreateTask, db : Session = Depends(get_db)):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=list[TaskResponse])
def list_task(db: Session = Depends(get_db)):
    return db.query(Task).all()