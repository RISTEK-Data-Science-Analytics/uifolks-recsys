from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ..base_recommender import BaseRecommender

class ContentBasedFeedRecommender(BaseRecommender):
    def __init__(self, feed_content):
        self.feed_content = feed_content
        self.vectorizer = TfidfVectorizer()
        self.feed_vectors = self.vectorizer.fit_transform(feed_content)

    def recommend(self, user_id: str, user_interests: str, top_n: int = 5):
        """ Recommend feeds based on content similarity """
        user_vector = self.vectorizer.transform([user_interests])
        similarity_scores = cosine_similarity(user_vector, self.feed_vectors)[0]
        ranked_feed_indices = similarity_scores.argsort()[-top_n:][::-1]
        return ranked_feed_indices