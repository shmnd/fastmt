from fastapi import FastAPI
from app.api import project,user,task,auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(project.router)
app.include_router(task.router)