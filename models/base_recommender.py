from abc import ABC, abstractmethod

class BaseRecommender(ABC):
    @abstractmethod
    def recommend(self, user_id: str, top_n: int = 5):
        """
        Recommend items (feeds or connections) for a user.
        :param user_id: The ID of the user to make recommendations for.
        :param top_n: Number of items to recommend.
        :return: A list of recommended item IDs.
        """
        pass