from fastapi import APIRouter, Depends
from uuid import UUID

from ..services.manager import ManagerService
from ..schemas.manager import Manager, ManagerCreate

from ..utils.service_result import handle_result

from ..config.database import get_db

router = APIRouter(
    prefix="/manager",
    tags=["Manager"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=Manager, operation_id="some_specific_id_you_define")
async def create_item(item: ManagerCreate, db: get_db = Depends()):
    result = ManagerService(db).create_item(item)
    return handle_result(result)


@router.get("", response_model=Manager)
async def get_item(id: UUID, db: get_db = Depends()):
    result = ManagerService(db).get_item(id)
    return handle_result(result)


# @router.put("", response_model=Manager)
# async def get_item(id: UUID, db: get_db = Depends()):
#     result = ManagerService(db).update_item(id)
#     return handle_result(result)
