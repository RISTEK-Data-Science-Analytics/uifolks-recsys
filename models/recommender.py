from .connection_recommender.connection_factory import ConnectionRecommenderFactory
from .feed_recommender.feed_factory import FeedRecommenderFactory
from .ensembler import Ensembler

def recommend_connections(user_id, algorithms, user_connections=None, interaction_matrix=None, top_n=5):
    recommenders = [ConnectionRecommenderFactory.get_recommender(algo, user_connections, interaction_matrix) for algo in algorithms]
    ensembler = Ensembler(recommenders)
    return ensembler.recommend(user_id, top_n)

def recommend_feeds(user_id, algorithms, interaction_matrix=None, feed_content=None, top_n=5):
    recommenders = [FeedRecommenderFactory.get_recommender(algo, interaction_matrix, feed_content) for algo in algorithms]
    ensembler = Ensembler(recommenders)
    return ensembler.recommend(user_id, top_n)