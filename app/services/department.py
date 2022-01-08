from uuid import UUID

from ..schemas.department import DepartmentCreate, DepartmentUpdate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.department import Department
from ..utils.service_result import ServiceResult


class DepartmentService(AppService):
    def create_department(self, project_id: UUID, item: DepartmentCreate) -> ServiceResult:
        department = DepartmentCRUD(
            self.db).create_department(item, project_id)
        return ServiceResult(department)

    def get_all_departments(self, project_id: UUID) -> ServiceResult:
        departments = DepartmentCRUD(self.db).get_all_departments(project_id)
        return ServiceResult(departments)

    def get_department(self, item_id: UUID) -> ServiceResult:
        department = DepartmentCRUD(self.db).get_department(item_id)
        if department is None:
            return ServiceResult(AppException.DepartmentNotFound())
        return ServiceResult(department)

    def update_department(self, item_id: UUID, item: DepartmentUpdate) -> ServiceResult:
        department = DepartmentCRUD(self.db).update_department(item_id, item)
        if department is None:
            return ServiceResult(AppException.DepartmentNotFound())
        return ServiceResult(department)


class DepartmentCRUD(AppCRUD):
    def create_department(self, item: DepartmentCreate, project_id: UUID) -> Department:
        department = Department(
            name=item.name, description=item.description, project_id=project_id)
        self.db.add(department)
        self.db.commit()
        self.db.refresh(department)
        return department

    def get_all_departments(self, project_id: UUID) -> Department:
        department = self.db.query(Department).filter(
            Department.project_id == project_id).all()
        if department:
            return department
        return None

    def get_department(self, item_id: UUID) -> Department:
        department = self.db.query(Department).filter(
            Department.id == item_id).first()
        if department:
            return department
        return None

    def update_department(self, item_id: UUID, item: DepartmentUpdate) -> Department:
        department = self.db.query(Department).filter(
            Department.id == item_id).first()
        if department is None:
            return None
        for var, value in vars(item).items():
            setattr(department, var, value) if value else None
        self.db.add(department)
        self.db.commit()
        self.db.refresh(department)
        return department
