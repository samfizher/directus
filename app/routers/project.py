from fastapi import APIRouter, Depends
from uuid import UUID

from ..services.project import ProjectService
from ..schemas.project import Project, ProjectCreate, ProjectUpdate

from ..services.department import DepartmentService
from ..schemas.department import Department, DepartmentCreate

from ..utils.service_result import handle_result
from ..utils.auth_handler import AuthHandler

from ..config.database import get_db

router = APIRouter(
    prefix="/project",
    tags=["Project"],
    responses={404: {"description": "Not found"}},
)
auth_handler = AuthHandler()


# create a new project
@router.post("", response_model=Project, response_description="Project created")
async def create_project(item: ProjectCreate, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = ProjectService(db).create_project(manager_id, item)
    return handle_result(result)


# get all projects
@router.get("", response_model=list[Project], response_description="Project data received")
async def get_all_projects(manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = ProjectService(db).get_all_projects(manager_id)
    return handle_result(result)


# get project data
@router.get("/{id}", response_model=Project, response_description="Project data received")
async def get_project(id: UUID, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = ProjectService(db).get_project(id)
    return handle_result(result)


# update project data
@router.put("/{id}", response_model=Project, response_description="Project data updated")
async def update_project(id: UUID, item: ProjectUpdate, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = ProjectService(db).update_project(id, item)
    return handle_result(result)


# create a new department
@router.post("/{id}/department", response_model=Department, response_description="Department created")
async def create_department(id: UUID, item: DepartmentCreate, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = DepartmentService(db).create_department(id, item)
    return handle_result(result)


# get all departments
@router.get("/{id}/department", response_model=list[Department], response_description="Department data received")
async def get_all_departments(id: UUID, manager_id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = DepartmentService(db).get_all_departments(id)
    return handle_result(result)