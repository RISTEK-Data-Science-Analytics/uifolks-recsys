from sklearn.decomposition import TruncatedSVD
import numpy as np
from ..base_recommender import BaseRecommender

class CollaborativeConnectionRecommender(BaseRecommender):
    def __init__(self, interaction_matrix):
        self.interaction_matrix = interaction_matrix
        self.svd = TruncatedSVD(n_components=50)
        self.user_factors = None

    def train(self):
        """ Train the collaborative filtering model using SVD """
        self.user_factors = self.svd.fit_transform(self.interaction_matrix)

    def recommend(self, user_id: int, top_n: int = 5):
        """ Recommend connections based on user interaction data """
        user_vector = self.user_factors[user_id]
        scores = np.dot(self.user_factors, user_vector)
        ranked_user_indices = np.argsort(-scores)[:top_n]
        return ranked_user_indices