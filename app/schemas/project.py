from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class ProjectBase(BaseModel):
    name: str
    description: str
    project_date: datetime
    shooting_date: datetime
    manager_id: UUID


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str]
    project_date: datetime
    shooting_date: datetime


class ProjectUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    project_date: Optional[datetime]
    shooting_date: Optional[datetime]


class Project(ProjectBase):
    # UUID
    id: UUID

    class Config:
        orm_mode = True
