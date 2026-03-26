from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.project import Project
from app.db.database import get_db
from app.schemas.project import ProjectCreate, ProjectResponse

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectResponse)
def create_project(project: )
