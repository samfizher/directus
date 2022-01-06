from uuid import UUID

from ..schemas.manager import ManagerCreate, ManagerInfo
from ..utils.app_exceptions import AppException
from ..utils.auth_handler import AuthHandler

from ..services.main import AppService, AppCRUD
from ..models.manager import Manager
from ..utils.service_result import ServiceResult
from ..utils.auth_handler import AuthHandler


class ManagerService(AppService):
    def create_manager(self, item: ManagerCreate) -> ServiceResult:
        manager = ManagerCRUD(self.db).get_manager_by_mail(item.mail)
        if manager is not None:
            return ServiceResult(AppException.EmailAlreadyExists())
        manager = ManagerCRUD(self.db).create_manager(item)
        return ServiceResult(manager)

    def get_manager(self, item_id: UUID) -> ServiceResult:
        manager = ManagerCRUD(self.db).get_manager(item_id)
        if manager is None:
            return ServiceResult(AppException.ManagerNotFound())
        return ServiceResult(manager)

    def update_manager(self, item_id: UUID, item: ManagerInfo) -> ServiceResult:
        manager = ManagerCRUD(self.db).update_manager(item_id, item)
        if manager is None:
            return ServiceResult(AppException.ManagerNotFound())
        return ServiceResult(manager)


class ManagerCRUD(AppCRUD):
    def create_manager(self, item: ManagerCreate) -> Manager:
        auth_handler = AuthHandler()
        manager = Manager(first_name=item.first_name, last_name=item.last_name,
                          mail=item.mail, password=auth_handler.get_password_hash(item.password))
        self.db.add(manager)
        self.db.commit()
        self.db.refresh(manager)
        return manager

    def get_manager(self, item_id: UUID) -> Manager:
        manager = self.db.query(Manager).filter(Manager.id == item_id).first()
        if manager:
            return manager
        return None

    def get_manager_by_mail(self, mail: str) -> Manager:
        manager = self.db.query(Manager).filter(Manager.mail == mail).first()
        if manager:
            return manager
        return None

    def update_manager(self, item_id: UUID, item: ManagerInfo) -> Manager:
        manager = self.db.query(Manager).filter(Manager.id == item_id).first()
        if manager is None:
            return None
        for var, value in vars(item).items():
            setattr(manager, var, value) if value else None
        self.db.add(manager)
        self.db.commit()
        self.db.refresh(manager)
        return manager
