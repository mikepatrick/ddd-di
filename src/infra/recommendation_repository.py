from src.domain.aggregate import AbstractRecommendationGetter
from uuid import UUID


class RecommendationRepository(AbstractRecommendationGetter):
    offer_id: UUID

    def __init__(self, offer_id):
        self.offer_id = offer_id

    def get_recommendation(self) -> str:
        """Call subscription domain"""
        return f'acquisition_{self.offer_id}'
