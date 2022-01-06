from fastapi import APIRouter, Depends
from uuid import UUID

from ..services.manager import ManagerService
from ..schemas.manager import Manager, ManagerCreate, ManagerUpdate

from ..utils.service_result import handle_result
from ..utils.auth_handler import AuthHandler

from ..config.database import get_db

router = APIRouter(
    prefix="/manager",
    tags=["Manager"],
    responses={404: {"description": "Not found"}},
)
auth_handler = AuthHandler()


# register as a new manager
@router.post("", response_model=Manager, response_description="Manager registered")
async def register_manager(item: ManagerCreate, db: get_db = Depends()):
    result = ManagerService(db).create_manager(item)
    return handle_result(result)


# get manager data
@router.get("", response_model=Manager, response_description="Manager data received")
async def get_manager(id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = ManagerService(db).get_manager(id)
    return handle_result(result)


# update manager data
@router.put("", response_model=Manager, response_description="Manager data updated")
async def update_manager(item: ManagerUpdate, id: UUID = Depends(auth_handler.auth_wrapper), db: get_db = Depends()):
    result = ManagerService(db).update_manager(id, item)
    return handle_result(result)
