import networkx as nx
from ..base_recommender import BaseRecommender

class GraphConnectionRecommender(BaseRecommender):
    def __init__(self, user_connections):
        self.graph = nx.Graph()
        self.graph.add_edges_from(user_connections)

    def recommend(self, user_id: str, top_n: int = 5):
        """ Recommend connections using Adamic-Adar Index """
        adamic_adar = nx.adamic_adar_index(self.graph, [(user_id, other) for other in self.graph.nodes if other != user_id and not self.graph.has_edge(user_id, other)])
        recommendations = sorted(adamic_adar, key=lambda x: -x[2])[:top_n]
        return [rec[1] for rec in recommendations]