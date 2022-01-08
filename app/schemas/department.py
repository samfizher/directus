from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class DepartmentBase(BaseModel):
    name: str
    description: str
    project_id: UUID


class DepartmentCreate(BaseModel):
    name: str
    description: Optional[str]


class DepartmentUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class Department(DepartmentBase):
    # UUID
    id: UUID

    class Config:
        orm_mode = True
