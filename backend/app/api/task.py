from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.db.database import get_db
from app.schemas.task import CreateTask, TaskResponse, TaskAssign, TaskStatusUpdate
from app.core.security import get_current_user

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


@router.put("/{task_id}/assign", response_model=TaskResponse)
def assign_task(
    task_id: int,
    data: TaskAssign,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.assigned_to = data.assigned_to

    db.commit()
    db.refresh(task)

    return task


@router.put("/{task_id}/status")
def update_status(
    task_id: int,
    data: TaskStatusUpdate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = data.status

    db.commit()
    db.refresh(task)

    return {"message": "Status updated"}



@router.get("/", response_model=list[TaskResponse])
def list_tasks(
    project_id: int = None,
    status: str = None,
    assigned_to: int = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    query = db.query(Task)

    if project_id:
        query = query.filter(Task.project_id == project_id)

    if status:
        query = query.filter(Task.status == status)

    if assigned_to:
        query = query.filter(Task.assigned_to == assigned_to)

    return query.offset(skip).limit(limit).all()