from sklearn.decomposition import TruncatedSVD
import numpy as np
from ..base_recommender import BaseRecommender

class CollaborativeFeedRecommender(BaseRecommender):
    def __init__(self, interaction_matrix):
        self.interaction_matrix = interaction_matrix
        self.svd = TruncatedSVD(n_components=50)
        self.user_factors = None
        self.feed_factors = None

    def train(self):
        """ Train the collaborative filtering model using SVD """
        self.user_factors = self.svd.fit_transform(self.interaction_matrix)
        self.feed_factors = self.svd.components_.T

    def recommend(self, user_id: int, top_n: int = 5):
        """ Recommend feeds based on collaborative filtering """
        user_vector = self.user_factors[user_id]
        scores = np.dot(self.feed_factors, user_vector)
        ranked_feed_indices = np.argsort(-scores)[:top_n]
        return ranked_feed_indices