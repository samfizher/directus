from uuid import UUID

from ..schemas.project import ProjectCreate, ProjectUpdate
from ..utils.app_exceptions import AppException

from ..services.main import AppService, AppCRUD
from ..models.project import Project
from ..utils.service_result import ServiceResult


class ProjectService(AppService):
    def create_project(self, manager_id: UUID, item: ProjectCreate) -> ServiceResult:
        project = ProjectCRUD(self.db).create_project(item, manager_id)
        return ServiceResult(project)

    def get_all_projects(self, manager_id: UUID) -> ServiceResult:
        projects = ProjectCRUD(self.db).get_all_projects(manager_id)
        return ServiceResult(projects)

    def get_project(self, item_id: UUID) -> ServiceResult:
        project = ProjectCRUD(self.db).get_project(item_id)
        if project is None:
            return ServiceResult(AppException.ProjectNotFound())
        return ServiceResult(project)

    def update_project(self, item_id: UUID, item: ProjectUpdate) -> ServiceResult:
        project = ProjectCRUD(self.db).update_project(item_id, item)
        if project is None:
            return ServiceResult(AppException.ProjectNotFound())
        return ServiceResult(project)


class ProjectCRUD(AppCRUD):
    def create_project(self, item: ProjectCreate, manager_id: UUID) -> Project:
        project = Project(name=item.name, description=item.description,
                          project_date=item.project_date, shooting_date=item.shooting_date, manager_id=manager_id)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get_all_projects(self, manager_id: UUID) -> Project:
        project = self.db.query(Project).filter(Project.manager_id == manager_id).all()
        if project:
            return project
        return None

    def get_project(self, item_id: UUID) -> Project:
        project = self.db.query(Project).filter(Project.id == item_id).first()
        if project:
            return project
        return None

    def update_project(self, item_id: UUID, item: ProjectUpdate) -> Project:
        project = self.db.query(Project).filter(Project.id == item_id).first()
        if project is None:
            return None
        for var, value in vars(item).items():
            setattr(project, var, value) if value else None
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project
