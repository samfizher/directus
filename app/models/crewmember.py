from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from ..config.database import Base


class Project(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, index=True)
    first_name  = Column(String)
    last_name  = Column(String)
    job_title = Column(String)
    is_lead = Column(Boolean)
    checked_in = Column(Boolean)
    department_id = Column(Integer, ForeignKey("department.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
