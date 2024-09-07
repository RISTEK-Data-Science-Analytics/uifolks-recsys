from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user import UserCreate, User

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate):
        """Create a new user."""
        user = UserModel(**user_data.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: str):
        """Retrieve a user by user ID and include interest_ids and achievement_ids."""
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            return None
        return self.transform_user(user)
    
    def get_all_users(self):
        """Retrieve all users and include achievement_ids."""
        users = self.db.query(UserModel).all()
        return [self.transform_user(user) for user in users]

    def transform_user(self, user):
        """Transform a user object to include achievement_ids."""
        achievement_ids = [achievement.id for achievement in user.achievements]  # Extract achievement IDs
        return {
            "user_id": user.id,
            "username": user.username,
            "fakultas": user.fakultas,
            "jurusan": user.jurusan,
            "angkatan": user.angkatan,
            "name": user.name,
            "bio": user.bio,
            "interest_ids": user.interest_ids,
            "achievement_ids": achievement_ids
        }