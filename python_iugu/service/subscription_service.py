from python_iugu.request.subscription_request import SubscriptionRequest

from python_iugu.model.subscription_model import SubscriptionModel, SubscriptionsModel
import deserialize
from typing import Dict, Any
from python_iugu.service.base_service import BaseService


class SubscriptionService(BaseService):
    _SUFFIX = "subscriptions"

    def create(self, subscription: SubscriptionRequest) -> SubscriptionModel:
        response = self.client.post(self._SUFFIX, subscription)
        return self._deserialize(SubscriptionModel, response)

    def search(self, id: str) -> SubscriptionModel:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return deserialize.deserialize(SubscriptionModel, response)

    def change(self, id: str, subscription: SubscriptionRequest) -> SubscriptionModel:
        response = self.client.put("%s/%s" % (self._SUFFIX, id), subscription)
        return self._deserialize(SubscriptionModel, response)

    def remove(self, id: str):
        response = self.client.delete("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(SubscriptionModel, response)

    def list(self, query_params: Dict[str, Any] = None) -> SubscriptionsModel:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(SubscriptionsModel, response)
