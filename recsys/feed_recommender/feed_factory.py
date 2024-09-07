from .collaborative import CollaborativeFeedRecommender
from .content_based import ContentBasedFeedRecommender

class FeedRecommenderFactory:
    @staticmethod
    def get_recommender(algorithm: str, interaction_matrix=None, feed_content=None):
        if algorithm == 'collaborative':
            return CollaborativeFeedRecommender(interaction_matrix)
        elif algorithm == 'content_based':
            return ContentBasedFeedRecommender(feed_content)
        else:
            raise ValueError(f"Unknown algorithm: {algorithm}")