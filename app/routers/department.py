from fastapi import APIRouter, Depends
from uuid import UUID

from ..services.department import DepartmentService
from ..schemas.department import Department, DepartmentUpdate

from ..services.crewmember import CrewmemberService
from ..schemas.crewmember import Crewmember, CrewmemberCreate

from ..utils.service_result import handle_result
from ..utils.auth_handler import AuthHandler

from ..config.database import get_db

router = APIRouter(
    prefix="/department",
    tags=["Department"],
    responses={404: {"description": "Not found"}},
)
auth_handler = AuthHandler()


# get department data
@router.get("/{id}", response_model=Department, response_description="Department data received")
async def get_department(id: UUID, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = DepartmentService(db).get_department(id)
    return handle_result(result)


# update department data
@router.put("/{id}", response_model=Department, response_description="Department data updated")
async def update_department(id: UUID, item: DepartmentUpdate, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = DepartmentService(db).update_department(id, item)
    return handle_result(result)


# create a new crewmember
@router.post("/{id}/crewmember", response_model=Crewmember, response_description="Crewmember created")
async def create_crewmember(id: UUID, item: CrewmemberCreate, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = CrewmemberService(db).create_crewmember(id, item)
    return handle_result(result)


# get all crewmembers
@router.get("/{id}/crewmember", response_model=list[Crewmember], response_description="Crewmember data received")
async def get_all_crewmembers(id: UUID, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = CrewmemberService(db).get_all_crewmembers(id)
    return handle_result(result)
