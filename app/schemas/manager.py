from pydantic import BaseModel
from uuid import UUID


class ManagerBase(BaseModel):
    first_name: str
    last_name: str
    mail: str


class ManagerCreate(ManagerBase):
    password: str


class Manager(ManagerBase):
    # UUID
    id: UUID

    class Config:
        orm_mode = True
