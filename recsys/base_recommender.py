from abc import ABC, abstractmethod
from typing import List

from schemas.user import User

class BaseRecommender(ABC):
    @abstractmethod
    def recommend(self, user: User, top_n: int = 5) -> List[User]:
        """
        Recommend items (feeds or connections) for a user.
        :param user: The user to make recommendations for.
        :param top_n: Number of items to recommend.
        :return: A list of recommended users.
        """
        raise NotImplementedError