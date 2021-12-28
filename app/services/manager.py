from uuid import UUID

from ..schemas.manager import ManagerCreate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.manager import Manager
from ..utils.service_result import ServiceResult


class ManagerService(AppService):
    def create_item(self, item: ManagerCreate) -> ServiceResult:
        manager = ManagerCRUD(self.db).create_item(item)
        # TODO create exception
        # if not manager:
        #     return ServiceResult(AppException.FooCreateItem())
        return ServiceResult(manager)

    def get_item(self, item_id: UUID) -> ServiceResult:
        manager = ManagerCRUD(self.db).get_item(item_id)
        # TODO create exceptions
        # if not foo_item:
        #     return ServiceResult(AppException.FooGetItem({"item_id": item_id}))
        # if not foo_item.public:
        #     return ServiceResult(AppException.FooItemRequiresAuth())
        return ServiceResult(manager)

    # TODO add update function


class ManagerCRUD(AppCRUD):
    def create_item(self, item: ManagerCreate) -> Manager:
        # TODO check if email existing
        # TODO add password hashing
        manager = Manager(first_name=item.first_name,
                          last_name=item.last_name, mail=item.mail, password=item.password)
        self.db.add(manager)
        self.db.commit()
        self.db.refresh(manager)
        return manager

    def get_item(self, item_id: UUID) -> Manager:
        manager = self.db.query(Manager).filter(Manager.id == item_id).first()
        if manager:
            return manager
        return None
