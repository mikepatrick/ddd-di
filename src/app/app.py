from infra.recommendation_repository import RecommendationRepository
from src.domain.aggregate import Order
from src.infra.customer_repository import CustomerRepository, CustomerRequest
from uuid import uuid4


def do_stuff():
    order = Order(id=uuid4())

    customer_request = CustomerRequest(foo='foo')
    cust_repo = CustomerRepository(customer_request)
    order.get_customer(cust_repo)

    subs_repo = RecommendationRepository(uuid4())
    recommendation = order.get_recommendation(subs_repo)
    if recommendation == 'reject':
        return

    do_more_stuff()


if __name__ == '__main__':
    do_stuff()


def do_more_stuff():
    pass
