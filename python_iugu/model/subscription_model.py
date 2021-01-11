from __future__ import annotations

from dataclasses import dataclass
import deserialize
import datetime
from python_iugu.utils import iso_to_datetime
from typing import Optional, List


@deserialize.parser("expires_at", iso_to_datetime)
@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@dataclass
class SubscriptionModel:
    id: str
    suspended: bool
    plan_identifier: str
    price_cents: int
    currency: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    customer_name: str
    customer_email: str
    credits_min: int
    customer_id: str
    plan_name: str
    customer_ref: str
    plan_ref: str
    active: bool
    credits: int
    credits_based: bool
    expires_at: Optional[datetime.datetime] = None
    subitems: Optional[List[SubItemsModel]] = None
    # cycled_at: None
    # credits_cycle
    # in_trial
    # recent_invoices


@dataclass
class SubItemsModel:
    id: str
    description: str
    quantity: int
    price_cents: int
    price: str
    total: str


@deserialize.key("total_items", "totalItems")
@dataclass
class SubscriptionsModel:
    total_items: int
    items: List[SubscriptionModel]
