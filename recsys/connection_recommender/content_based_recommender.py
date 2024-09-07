from typing import List, Dict
from typing_extensions import Annotated
from recsys.base_recommender import BaseRecommender
from schemas.recommender_input import ConnectionRecommenderInput
from schemas.user import User

class ContentBasedRecommender(BaseRecommender):
    """
    A content-based filtering algorithm that recommends users based on shared faculty, major, interests, and achievement types.
    """
    def __init__(self, data: ConnectionRecommenderInput, weights: Dict[str, float] = None):
        """Initialize the recommender with the list of all users and optional weights."""
        self.all_users = data.all_users
        
        self.weights = weights or {
            'faculty': 0.25,
            'major': 0.25, 
            'interests': 0.25,
            'achievements': 0.25
        }

    def calculate_similarity(self, user1: User, user2: User) -> float:
        """Calculate similarity score between two users based on faculty, major, interests, and achievements."""
        similarity_score = 0.0

        # Faculty match
        if user1.fakultas == user2.fakultas:
            similarity_score += self.weights['faculty']

        # Major match
        if user1.jurusan == user2.jurusan:
            similarity_score += self.weights['major']

        # Interest matching: calculate common interests
        common_interests = len(set(user1.interest_ids) & set(user2.interest_ids))
        total_interests = len(set(user1.interest_ids) | set(user2.interest_ids))
        if total_interests > 0:
            interest_similarity = common_interests / total_interests
            similarity_score += interest_similarity * self.weights['interests']

        # TODO: Revise this achievement based matching so it compares by achievement type, not id.
        common_achievements = len(set(user1.achievement_ids) & set(user2.achievement_ids))
        total_achievements = len(set(user1.achievement_ids) | set(user2.achievement_ids))
        if total_achievements > 0:
            achievement_similarity = common_achievements / total_achievements
            similarity_score += achievement_similarity * self.weights['achievements']

        return similarity_score

    def recommend(self, user: User, top_n: int = 5) -> List[User]:
        """Recommend top N users based on similarity to the current user."""
        recommendations = []
        
        for other_user in self.all_users:
            if other_user.user_id != user.user_id:
                similarity_score = self.calculate_similarity(user, other_user)
                recommendations.append((other_user, similarity_score))
        
        recommendations.sort(key=lambda x: -x[1])
        return [rec[0] for rec in recommendations[:top_n]]