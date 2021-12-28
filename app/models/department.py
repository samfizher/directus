from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from ..config.database import Base


class Project(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    project_id = Column(Integer, ForeignKey("project.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
