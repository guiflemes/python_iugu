from __future__ import annotations
from dataclasses import dataclass
import deserialize
from python_iugu.utils import iso_to_datetime
import datetime
from typing import List, Optional
from python_iugu import enuns


@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@dataclass
class PlanModel:
    id: str
    name: str
    identifier: str
    interval: int
    interval_type: enuns.IntervalType
    created_at: datetime.datetime
    updated_at: datetime.datetime
    prices: List[Price]
    features: Optional[List[Feature]]
    payable_with: enuns.PayableWith
    max_cycles: int


@deserialize.key("total_items", "totalItems")
@dataclass
class PlansModel:
    total_items: int
    items: List[PlanModel]


@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@dataclass
class Price:
    id: str
    plan_id: str
    currency: str
    value_cents: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@dataclass
class Feature:
    id: str
    name: str
    identifier: str
    plan_id: str
    position: int
    value: int
    important: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
