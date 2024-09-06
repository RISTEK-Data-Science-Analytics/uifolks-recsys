from .graph import GraphConnectionRecommender
from .collaborative import CollaborativeConnectionRecommender

class ConnectionRecommenderFactory:
    @staticmethod
    def get_recommender(algorithm: str, user_connections=None, interaction_matrix=None):
        if algorithm == 'graph':
            return GraphConnectionRecommender(user_connections)
        elif algorithm == 'collaborative':
            return CollaborativeConnectionRecommender(interaction_matrix)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")