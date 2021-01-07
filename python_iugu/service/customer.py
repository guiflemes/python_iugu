from typing import Dict, Any

from python_iugu.expcetion import RequiredParameter
from python_iugu.service.base import BaseService
from python_iugu.model.customer import Customer, Customers
from python_iugu.request.customer import CustomerRequest


class CustomerService(BaseService):
    _SUFFIX = "customers"

    def create(self, customer: CustomerRequest) -> Customer:
        if customer.email is None:
            raise RequiredParameter('Customer email not informed')

        response = self.client.post(self._SUFFIX, customer)
        return self._deserialize(Customer, response)

    def find(self, id: str) -> Customer:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(Customer, response)

    def change(self, id: str, customer: CustomerRequest) -> Customer:
        response = self.client.put("%s/%s" % (self._SUFFIX, id), customer)
        return self._deserialize(Customer, response)

    def remove(self, id: str) -> Customer:
        response = self.client.delete("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(Customer, response)

    def list(self, query_params: Dict[str, Any] = None) -> Customers:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(Customers, response)
