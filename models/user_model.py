import uuid
# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from db import Base
from models.association_tables import user_achievement_association  # Import association table

class UserModel(Base):
    __tablename__ = "users"

    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True) # When switching to postgres
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True)
    fakultas = Column(String)
    jurusan = Column(String)
    angkatan = Column(Integer)
    name = Column(String)
    bio = Column(String)

    # Storing interest_ids as a JSON field (list of integers)
    interest_ids = Column(JSON, nullable=False)

    # Many-to-many relationship with achievements
    achievements = relationship(
        "AchievementModel",
        secondary=user_achievement_association,  # Use association table
        back_populates="users"
    )

    def __repr__(self):
        return f"<User(username={self.username}, name={self.name})>"