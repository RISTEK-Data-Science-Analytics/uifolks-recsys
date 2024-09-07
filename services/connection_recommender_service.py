from typing import List
from sqlalchemy.orm import Session
from services.connection_data_service import ConnectionDataService
from recsys import recommender
from schemas.recommender_input import ConnectionRecommenderInput
from services.user_service import UserService

class ConnectionRecommenderService:
    def __init__(self, db: Session):
        self.db = db
        self.user_service = UserService(db)
        self.data_service = ConnectionDataService(db)

    def recommend_connections(self, user_id: str, algorithms: List[str]):
        """Recommend connections using selected algorithms."""
        data = ConnectionRecommenderInput(
            user=self.user_service.get_user_by_id(str(user_id)),
            all_users=self.user_service.get_all_users(),
            user_connections=self.data_service.get_user_connections(user_id),
            all_connections=self.data_service.get_all_connections(),
            interaction_matrix=None,
            top_n=5,
        )
        return recommender.recommend_connections(algorithms, data)