from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base
from models.association_tables import user_achievement_association
import uuid
# from sqlalchemy.dialects.postgresql import UUID

class AchievementModel(Base):
    __tablename__ = "achievements"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) # When switching to postgres
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    issued_date = Column(DateTime, nullable=False)
    field = Column(Integer, nullable=False)
    issuer = Column(String, nullable=False)

    users = relationship(
        "UserModel",
        secondary=user_achievement_association,
        back_populates="achievements"
    )

    def __repr__(self):
        return f"<Achievement(title={self.title}, field={self.field})>"