from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.project import Project
from app.db.database import get_db
from app.schemas.project import ProjectCreate, ProjectResponse

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectCreate)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.get("/", response_model=list[ProjectResponse])
def list_projects(project: ProjectResponse, db: Session = Depends(get_db)):
    return db.query(Project).all()



@router.put("/{project_id}")
def update_project(project_id: int, project: ProjectCreate, db: Session = Depends(get_db)):

    db_project = db.query(Project).get(project_id)

    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found ")
    
    for key, value in Project.dict().items():
        setattr(db_project, key, value)

    db.commit()
    return {'message':"Updated success"}


@router.delete("/{project_id}") 
def delete_projects(project_id: int, db: Session = Depends(get_db)):
    db_project = db.query(Project).get(project_id)

    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    db.delete(db_project)
    db.commit()
    return {'message':'Deleted success'}
