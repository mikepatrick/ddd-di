from pydantic import BaseModel
from uuid import UUID, uuid4

from abc import ABC, abstractmethod
from typing import Optional


class Customer(BaseModel):
    """Customer shape for Fact/API response"""
    id: UUID
    foo_bar: str


class AbstractCustomerGetter(ABC):
    @abstractmethod
    def get_customer(self) -> Customer:
        pass


class AbstractRecommendationGetter(ABC):
    @abstractmethod
    def get_recommendation(self, offer_id: UUID) -> str:
        pass


class Order(BaseModel):
    id: UUID
    purchaser: Optional[Customer]

    def get_customer(self, getter: AbstractCustomerGetter):
        self.purchaser = getter.get_customer()
        return self.purchaser

    def get_recommendation(self, getter: AbstractRecommendationGetter):
        return getter.get_recommendation(uuid4())

    def _get_recommendation(self, offer_id: UUID) -> str:
        if not self.purchaser:
            raise Exception('Recommendation requires purchaser')
        return f'aquisition_{offer_id}_{self.purchaser.id}_{self.purchaser.foo_bar}'
