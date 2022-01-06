from ..schemas.manager import ManagerCredentials, ManagerAuth
from ..utils.app_exceptions import AppException
from ..utils.auth_handler import AuthHandler

from ..services.main import AppService
from ..services.manager import ManagerCRUD
from ..utils.service_result import ServiceResult


class AuthService(AppService):
    def create_token(self, credentials: ManagerCredentials) -> ServiceResult:
        manager = ManagerCRUD(self.db).get_manager_by_mail(credentials.mail)
        auth_handler = AuthHandler()
        if manager is not None:
            if auth_handler.verify_password(credentials.password, manager.password):
                token = auth_handler.encode_token(manager.id)
                auth_details = ManagerAuth(token=token, id=manager.id)
                return ServiceResult(auth_details)
        return ServiceResult(AppException.InvalidLogin())
