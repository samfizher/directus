from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID


class ManagerBase(BaseModel):
    mail: EmailStr


class ManagerAuth(BaseModel):
    token: str
    id: UUID


class ManagerInfo(ManagerBase):
    first_name: str
    last_name: str


class ManagerCredentials(ManagerBase):
    password: str


class ManagerCreate(ManagerInfo):
    password: str


class ManagerUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]


class Manager(ManagerInfo):
    # UUID
    id: UUID

    class Config:
        orm_mode = True
