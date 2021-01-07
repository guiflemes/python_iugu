from typing import Dict, Any

from iugu.service.base import BaseService
from iugu.model.invoice import Invoice, Invoices
import deserialize
from iugu.request.invoice import InvoiceRequest


class InvoiceService(BaseService):
    _SUFFIX = "invoices"

    def create(self, invoice: InvoiceRequest) -> Invoice:
        response = self.client.post(self._SUFFIX, invoice)
        return self._deserialize(Invoice, response)

    def search(self, id: str) -> Invoice:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return deserialize.deserialize(Invoice, response)

    def cancel(self, id: str) -> Invoice:
        response = self.client.put("%s/%s/cancel" % (self._SUFFIX, id))
        return deserialize.deserialize(Invoice, response)

    def list(self, query_params: Dict[str, Any] = None) -> Invoices:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(Invoices, response)
