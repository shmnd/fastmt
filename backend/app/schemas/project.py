from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    description: str
    created_by: int

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str
    created_by: int

    class Config:
        from_attributes = True