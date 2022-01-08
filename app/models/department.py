from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from ..config.database import Base


class Department(Base):
    __tablename__ = "department"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    description = Column(String)
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
