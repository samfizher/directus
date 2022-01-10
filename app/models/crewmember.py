from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from ..config.database import Base


class Crewmember(Base):
    __tablename__ = "crewmember"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name  = Column(String)
    last_name  = Column(String)
    job_title = Column(String)
    is_lead = Column(Boolean)
    activated = Column(Boolean)
    checked_in = Column(Boolean)
    department_id = Column(UUID(as_uuid=True), ForeignKey("department.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
