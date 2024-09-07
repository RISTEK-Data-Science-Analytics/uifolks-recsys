from typing import List
from schemas.user import User
from .connection_recommender.connection_recommender_factory import ConnectionRecommenderFactory
from .feed_recommender.feed_factory import FeedRecommenderFactory
from .ensembler import Ensembler
from schemas.recommender_input import ConnectionRecommenderInput

def recommend_connections(
    algorithms: List[str], 
    data: ConnectionRecommenderInput,
) -> List[str]:
    recommenders = [ConnectionRecommenderFactory.get_recommender(algo, data) for algo in algorithms]
    ensembler = Ensembler(recommenders)
    return ensembler.recommend(data.user, data.top_n)

def recommend_feeds(user_id, algorithms, interaction_matrix=None, feed_content=None, top_n=5):
    recommenders = [FeedRecommenderFactory.get_recommender(algo, interaction_matrix, feed_content) for algo in algorithms]
    ensembler = Ensembler(recommenders)
    return ensembler.recommend(user_id, top_n)