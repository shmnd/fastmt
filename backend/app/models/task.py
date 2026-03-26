from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from app.db.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    status = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))
    assigned_to = Column(Integer, ForeignKey('users.id'))
    due_date = Column(DateTime)





