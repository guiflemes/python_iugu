from typing import Dict, Any

from python_iugu.service.base_service import BaseService
from python_iugu.model.invoice_model import InvoiceModel, InvoicesModel
import deserialize
from python_iugu.request.invoice_request import InvoiceRequest


class InvoiceService(BaseService):
    _SUFFIX = "invoices"

    def create(self, invoice: InvoiceRequest) -> InvoiceModel:
        response = self.client.post(self._SUFFIX, invoice)
        return self._deserialize(InvoiceModel, response)

    def search(self, id: str) -> InvoiceModel:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return deserialize.deserialize(InvoiceModel, response)

    def cancel(self, id: str) -> InvoiceModel:
        response = self.client.put("%s/%s/cancel" % (self._SUFFIX, id))
        return deserialize.deserialize(InvoiceModel, response)

    def list(self, query_params: Dict[str, Any] = None) -> InvoicesModel:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(InvoicesModel, response)
