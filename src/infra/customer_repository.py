from src.domain.aggregate import AbstractCustomerGetter
from pydantic import BaseModel
from src.domain.aggregate import Customer


class CustomerRequest(BaseModel):
    """Probably incoming request shape but possibly the customer domain request shape?"""
    foo: str


class CustomerResponse(BaseModel):
    """Customer domain response shape"""
    bar: str


class CustomerRepository(AbstractCustomerGetter):
    """CustomerRepository calls customer domain and returns the found or newly created Customer."""
    req: CustomerRequest

    def __init__(self, request: CustomerRequest):
        """Creating a CustomerRepository requires some request shape."""
        self.req = request

    def get_customer(self) -> Customer:
        result = self._process(self.req)
        return self._map_customer_domain_response_to_domain_shape(result)

    def _process(self, req: CustomerRequest) -> CustomerResponse:
        """Call customer domain"""
        return CustomerResponse(bar='bar')

    def _map_customer_domain_response_to_domain_shape(self, res: CustomerResponse) -> Customer:
        """ Map customer domain response shape to Customer shape that domain layer understands"""
        return Customer(foo_bar=f'foo_bar={res.bar}')
