from typing import Dict, Any
from python_iugu.service.base_service import BaseService
from python_iugu.model.plan_model import PlanModel, PlansModel
from python_iugu.request.plan_request import PlanRequest


class PlanService(BaseService):
    _SUFFIX = "plans"

    def create(self, plan: PlanRequest) -> PlanModel:
        response = self.client.post(self._SUFFIX, plan)
        return self._deserialize(PlanModel, response)

    def find(self, id: str) -> PlanModel:
        response = self.client.get("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(PlanModel, response)

    def find_by_identifier(self, identifier: str) -> PlanModel:
        response = self.client.get("%s/identifier/%s" % (self._SUFFIX, identifier))
        return self._deserialize(PlanModel, response)

    def change(self, id: str, plan: PlanRequest) -> PlanModel:
        response = self.client.put("%s/%s" % (self._SUFFIX, id), plan)
        return self._deserialize(PlanModel, response)

    def remove(self, id: str) -> PlanModel:
        response = self.client.delete("%s/%s" % (self._SUFFIX, id))
        return self._deserialize(PlanModel, response)

    def list(self, query_params: Dict[str, Any] = None) -> PlansModel:
        response = self.client.get(self._SUFFIX, query_params)
        return self._deserialize(PlansModel, response)
