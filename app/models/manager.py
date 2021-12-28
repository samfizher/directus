from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from passlib.context import CryptContext
import uuid

from ..config.database import Base


class Manager(Base):
    __tablename__ = "manager"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String)
    last_name = Column(String)
    mail = Column(String)
    password = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


    def verify_password(plain_password, hashed_password):
        return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(plain_password, hashed_password)


    def get_password_hash(password):
        return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(password)