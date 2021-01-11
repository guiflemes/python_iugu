from typing import Dict, Any

from python_iugu.expcetion import RequiredParameter
from python_iugu.service.base_service import BaseService
from python_iugu.model.customer_model import CustomerModel, CustomersModel
from python_iugu.request.customer_request import CustomerRequest


class CustomerService(BaseService):
    _SUFFIX = "customers"

    def create(self, customer: CustomerRequest) -> CustomerModel:
        if customer.email is None:
            raise RequiredParameter('Customer email not informed')

        response = self.client.post(self._SUFFIX, customer)
        return self._deserialize(CustomerModel, response)

    def find(self, id: str) -> CustomerModel:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(CustomerModel, response)

    def change(self, id: str, customer: CustomerRequest) -> CustomerModel:
        response = self.client.put("%s/%s" % (self._SUFFIX, id), customer)
        return self._deserialize(CustomerModel, response)

    def remove(self, id: str) -> CustomerModel:
        response = self.client.delete("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(CustomerModel, response)

    def list(self, query_params: Dict[str, Any] = None) -> CustomersModel:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(CustomersModel, response)
