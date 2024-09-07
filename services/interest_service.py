from sqlalchemy.orm import Session
from schemas.user import User
from models.user_model import UserModel
from constants.interest import interest

class InterestService:
    def __init__(self, db: Session):
        self.db = db

    def add_user_interest(self, user_id: int, interest_id: int):
        """Add an interest to a user profile."""
        if interest_id not in interest.keys():
            raise ValueError("Invalid interest ID")
        
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise ValueError("User not found")
        
        user.interests.append(interest_id)
        self.db.commit()
        return user

    def get_user_interests(self, user_id: int):
        """Get the interests for a user."""
        user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
        if user:
            return [interest[i] for i in user.interests]
        return []