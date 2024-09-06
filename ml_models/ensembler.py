class Ensembler:
    def __init__(self, algorithms, weights=None):
        """
        Initialize the ensembler with a list of algorithms and optional weights.
        :param algorithms: A list of recommendation algorithm instances.
        :param weights: A list of weights for score aggregation.
        """
        self.algorithms = algorithms
        self.weights = weights or [1 / len(algorithms)] * len(algorithms)  # Equal weighting if none provided

    def recommend(self, user_id, top_n=5):
        """ Ensemble recommendations using score aggregation """
        all_scores = self._get_all_recommendations(user_id, top_n)
        combined_scores = self._aggregate_scores(all_scores)
        sorted_recommendations = sorted(combined_scores.items(), key=lambda x: -x[1])
        return [item for item, _ in sorted_recommendations[:top_n]]

    def _get_all_recommendations(self, user_id, top_n):
        """ Get recommendations from all algorithms """
        all_scores = []
        for algo in self.algorithms:
            recommendations = algo.recommend(user_id, top_n)
            scores = {item: score for item, score in zip(recommendations, range(top_n, 0, -1))}  # Ranking as scores
            all_scores.append(scores)
        return all_scores

    def _aggregate_scores(self, all_scores):
        """ Aggregate scores using weighted average """
        combined_scores = {}
        for i, scores in enumerate(all_scores):
            weight = self.weights[i]
            for item, score in scores.items():
                if item in combined_scores:
                    combined_scores[item] += score * weight
                else:
                    combined_scores[item] = score * weight
        return combined_scores