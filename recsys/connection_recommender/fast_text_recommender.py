from typing import List
from recsys.base_recommender import BaseRecommender
from schemas.recommender_input import ConnectionRecommenderInput
from schemas.user import User
from constants.achievement_type import achievement_categories, achievement_type
from gensim.models import FastText
from models.achievement_model import AchievementModel
from db import SessionLocal

def get_achievement_text(user_achievement_ids: List[str]) -> str:
    db = SessionLocal()
    achievements = db.query(AchievementModel).filter(AchievementModel.id.in_(user_achievement_ids)).all()
    
    if not achievements:
        print("No achievements found for IDs: ", user_achievement_ids)
        return ""

    grouped_achievement_names = set()
    for achievement in achievements:
        field = achievement.field
        if field in achievement_type:
            achievement_name = achievement_type[field]
            for category, fields in achievement_categories.items():
                if achievement_name in fields:
                    grouped_achievement_names.add(category)

    print("Grouped Achievement Names: ", grouped_achievement_names)
    
    db.close()
    return " ".join(grouped_achievement_names) if grouped_achievement_names else ""

class FastTextRecommender(BaseRecommender):
    def __init__(self, data: ConnectionRecommenderInput):
        """
        Initialize the recommender with all users' data and database session.
        Train a FastText model based on the achievements.
        """
        self.all_users = data.all_users

        # Prepare user achievements for FastText training
        self.achievement_texts = [get_achievement_text(user.achievement_ids) for user in self.all_users]
        print("self achievements text: ", self.achievement_texts)

        # Tokenize the achievement texts (ensure it's a list of lists of tokens)
        tokenized_texts = [text.split() for text in self.achievement_texts]
        print("tokenized texts: ", tokenized_texts)
        
        if len(tokenized_texts) == 0 or not any(tokenized_texts):
            raise ValueError("The tokenized_texts list is empty or malformed.")

        # Create a FastText model
        self.model = FastText(vector_size=100, window=3, min_count=1)

        # Build the vocabulary based on tokenized texts
        self.model.build_vocab(corpus_iterable=tokenized_texts)

        # Train the FastText model
        self.model.train(corpus_iterable=tokenized_texts, total_examples=len(tokenized_texts), epochs=10)

    def get_user_vector(self, user: User) -> List[float]:
        """
        Convert a user's achievements into a FastText vector.
        """
        user_achievement_text = get_achievement_text(user.achievement_ids).split()
        return self.model.wv.get_mean_vector(user_achievement_text)

    def calculate_similarity(self, user1: User, user2: User) -> float:
        """
        Calculate cosine similarity between two users based on their FastText achievement vectors,
        and give extra weight to matching achievement categories.
        """
        vec1 = self.get_user_vector(user1)
        vec2 = self.get_user_vector(user2)

        # Cosine similarity between FastText vectors
        similarity_score = self.model.wv.cosine_similarities(vec1, [vec2])[0]

        # Get achievement categories for both users
        user1_categories = set(get_achievement_text(user1.achievement_ids).split())
        user2_categories = set(get_achievement_text(user2.achievement_ids).split())

        # Add a bonus to the similarity score if users share common achievement categories
        common_categories = user1_categories.intersection(user2_categories)
        category_bonus = len(common_categories) * 0.1

        return similarity_score + category_bonus

    def recommend(self, user: User, top_n: int = 5) -> List[User]:
        """
        Recommend top N users based on similarity to the given user.
        """
        recommendations = []
        
        for other_user in self.all_users:
            if other_user.user_id != user.user_id:
                similarity_score = self.calculate_similarity(user, other_user)
                recommendations.append((other_user, similarity_score))
        
        # Sort users based on similarity score in descending order
        recommendations.sort(key=lambda x: -x[1])
        return [rec[0] for rec in recommendations[:top_n]]
