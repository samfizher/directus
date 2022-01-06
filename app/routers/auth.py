from fastapi import APIRouter, Depends

from ..services.auth import AuthService
from ..schemas.manager import ManagerCredentials, ManagerAuth

from ..utils.service_result import handle_result

from ..config.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=ManagerAuth, response_description="Authentication Token received")
async def authenticate_manager(credentials: ManagerCredentials, db: get_db = Depends()):
    result = AuthService(db).create_token(credentials)
    return handle_result(result)
