from recsys.base_recommender import BaseRecommender
from schemas.recommender_input import ConnectionRecommenderInput
from .graph_based_recommender import GraphConnectionRecommender
from .content_based_recommender import ContentBasedRecommender
from recsys.hyperparameters import *

class ConnectionRecommenderFactory:
    @staticmethod
    def get_recommender(algorithm: str, data: ConnectionRecommenderInput) -> BaseRecommender:
        if algorithm == 'graph':
            return GraphConnectionRecommender(data)
        elif algorithm == 'content_based':
            return ContentBasedRecommender(data, **content_based_connection_hyperparams)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")