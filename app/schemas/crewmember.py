from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class CrewmemberBase(BaseModel):
    first_name: str
    last_name: str
    job_title: str
    is_lead: bool
    #activated: bool
    #checked_in: bool
    department_id: UUID


class CrewmemberSet(BaseModel):
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    job_title: Optional[str] = ""


class CrewmemberCreate(CrewmemberSet):
    is_lead: bool = False


class CrewmemberUpdate(CrewmemberSet):
    is_lead: Optional[bool] = False


class Crewmember(CrewmemberBase):
    # UUID
    id: UUID

    class Config:
        orm_mode = True
