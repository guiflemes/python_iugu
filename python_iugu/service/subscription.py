from python_iugu.request.subscription_request import SubscriptionRequest

from python_iugu.model.subscription import Subscription, Subscriptions
import deserialize
from typing import Dict, Any
from python_iugu.service.base import BaseService


class SubscriptionService(BaseService):
    _SUFFIX = "subscriptions"

    def create(self, subscription: SubscriptionRequest) -> Subscription:
        response = self.client.post(self._SUFFIX, subscription)
        return self._deserialize(Subscription, response)

    def search(self, id: str) -> Subscription:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return deserialize.deserialize(Subscription, response)

    def change(self, id: str, subscription: SubscriptionRequest) -> Subscription:
        response = self.client.put("%s/%s" % (self._SUFFIX, id), subscription)
        return self._deserialize(Subscription, response)

    def remove(self, id: str):
        response = self.client.delete("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(Subscription, response)

    def list(self, query_params: Dict[str, Any] = None) -> Subscriptions:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(Subscriptions, response)
