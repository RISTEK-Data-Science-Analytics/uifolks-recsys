from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
import uuid
# from sqlalchemy.dialects.postgresql import UUID
from db import Base

class ConnectionModel(Base):
    __tablename__ = "connections"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) # When switching to postgres
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    first_user_id = Column(String, index=True)
    second_user_id = Column(String, index=True)
    timestamp = Column(DateTime, server_default=func.now())  # Automatically set to current timestamp

    def __repr__(self):
        return f"<Connection(first_userid={self.first_user_id}, second_userid={self.second_user_id})>"