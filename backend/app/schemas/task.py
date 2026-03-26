from pydantic import BaseModel
from datetime import datetime

class CreateTask(BaseModel):
    title: str
    description: str
    status: str
    project_id: int
    assigned_to: int
    due_date: datetime

class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    project_id: int
    assigned_to: int
    due_date: datetime

    class Config:
        from_attributes = True