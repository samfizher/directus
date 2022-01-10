from fastapi import APIRouter, Depends
from uuid import UUID

from ..services.crewmember import CrewmemberService
from ..schemas.crewmember import Crewmember, CrewmemberCreate, CrewmemberUpdate

from ..services.department import DepartmentService
from ..schemas.department import Department, DepartmentCreate

from ..utils.service_result import handle_result
from ..utils.auth_handler import AuthHandler

from ..config.database import get_db

router = APIRouter(
    prefix="/crew",
    tags=["Crewmember"],
    responses={404: {"description": "Not found"}},
)
auth_handler = AuthHandler()


# get crewmember data
@router.get("/{id}", response_model=Crewmember, response_description="Crewmember data received")
async def get_crewmember(id: UUID, department_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = CrewmemberService(db).get_crewmember(id)
    return handle_result(result)


# update crewmember data
@router.put("/{id}", response_model=Crewmember, response_description="Crewmember data updated")
async def update_crewmember(id: UUID, item: CrewmemberUpdate, department_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = CrewmemberService(db).update_crewmember(id, item)
    return handle_result(result)
