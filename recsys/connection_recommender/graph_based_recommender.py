import networkx as nx

from schemas.user import User
from ..base_recommender import BaseRecommender
from schemas.recommender_input import ConnectionRecommenderInput

class GraphConnectionRecommender(BaseRecommender):
    def __init__(self, data: ConnectionRecommenderInput):
        self.graph = nx.Graph()
        self.graph.add_edges_from(data.all_connections)

        # Store all users for later lookup
        self.user_lookup = {user.user_id: user for user in data.all_users}

    def recommend(self, user: User, top_n: int = 5):
        """ Recommend connections using Adamic-Adar Index """
        if user.user_id not in self.graph:
            print(f"User {user.user_id} is not present in the graph or has no connections.")
            return []
        
        # Adamic-Adar index to calculate similarities
        adamic_adar = nx.adamic_adar_index(self.graph, [
            (user.user_id, other) for other in self.graph.nodes
            if other != user.user_id and not self.graph.has_edge(user.user_id, other)
        ])
        
        # Sort recommendations by score and limit to top_n
        recommendations = sorted(adamic_adar, key=lambda x: -x[2])[:top_n]
        
        # Return list of User objects by looking them up in user_lookup
        return [self.user_lookup[rec[1]] for rec in recommendations if rec[1] in self.user_lookup]