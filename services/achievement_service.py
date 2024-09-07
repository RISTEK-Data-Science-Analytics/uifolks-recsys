from sqlalchemy.orm import Session
from schemas.achievement import Achievement
from models.achievement_model import AchievementModel
from constants.achievement_type import achievement_type

class AchievementService:
    def __init__(self, db: Session):
        self.db = db

    def add_achievement(self, user_id: int, achievement_data: Achievement):
        """Add an achievement for a user."""
        if achievement_data.field not in achievement_type.keys():
            raise ValueError("Invalid achievement type")
        achievement = AchievementModel(**achievement_data.dict(), user_id=user_id)
        self.db.add(achievement)
        self.db.commit()
        self.db.refresh(achievement)
        return achievement

    def get_user_achievements(self, user_id: int):
        """Get all achievements for a user."""
        return self.db.query(AchievementModel).filter(AchievementModel.user_id == user_id).all()

    def delete_achievement(self, achievement_id: int):
        """Delete an achievement."""
        achievement = self.db.query(AchievementModel).filter(AchievementModel.id == achievement_id).first()
        if achievement:
            self.db.delete(achievement)
            self.db.commit()
        return achievement