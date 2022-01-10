from uuid import UUID

from ..schemas.crewmember import CrewmemberCreate, CrewmemberUpdate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.crewmember import Crewmember
from ..utils.service_result import ServiceResult


class CrewmemberService(AppService):
    def create_crewmember(self, department_id: UUID, item: CrewmemberCreate) -> ServiceResult:
        crewmember = CrewmemberCRUD(
            self.db).create_crewmember(item, department_id)
        return ServiceResult(crewmember)

    def get_all_crewmembers(self, department_id: UUID) -> ServiceResult:
        crewmembers = CrewmemberCRUD(
            self.db).get_all_crewmembers(department_id)
        return ServiceResult(crewmembers)

    def get_crewmember(self, item_id: UUID) -> ServiceResult:
        crewmember = CrewmemberCRUD(self.db).get_crewmember(item_id)
        if crewmember is None:
            return ServiceResult(AppException.CrewmemberNotFound())
        return ServiceResult(crewmember)

    def update_crewmember(self, item_id: UUID, item: CrewmemberUpdate) -> ServiceResult:
        crewmember = CrewmemberCRUD(self.db).update_crewmember(item_id, item)
        if crewmember is None:
            return ServiceResult(AppException.CrewmemberNotFound())
        return ServiceResult(crewmember)


class CrewmemberCRUD(AppCRUD):
    def create_crewmember(self, item: CrewmemberCreate, department_id: UUID) -> Crewmember:
        crewmember = Crewmember(first_name=item.first_name, last_name=item.last_name,
                                job_title=item.job_title, is_lead=item.is_lead, department_id=department_id)
        self.db.add(crewmember)
        self.db.commit()
        self.db.refresh(crewmember)
        return crewmember

    def get_all_crewmembers(self, department_id: UUID) -> Crewmember:
        crewmember = self.db.query(Crewmember).filter(
            Crewmember.department_id == department_id).all()
        if crewmember:
            return crewmember
        return None

    def get_crewmember(self, item_id: UUID) -> Crewmember:
        crewmember = self.db.query(Crewmember).filter(
            Crewmember.id == item_id).first()
        if crewmember:
            return crewmember
        return None

    def update_crewmember(self, item_id: UUID, item: CrewmemberUpdate) -> Crewmember:
        # TODO fix is_lead not possible being set to false
        crewmember = self.db.query(Crewmember).filter(
            Crewmember.id == item_id).first()
        if crewmember is None:
            return None
        for var, value in vars(item).items():
            setattr(crewmember, var, value) if value else None
        self.db.add(crewmember)
        self.db.commit()
        self.db.refresh(crewmember)
        return crewmember
