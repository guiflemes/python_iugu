from __future__ import annotations

from dataclasses import dataclass
import deserialize
import datetime

from python_iugu.model.custom_variable_model import CustomVariableModel
from python_iugu.utils import iso_to_datetime
from typing import Optional, List


@deserialize.parser("expires_at", iso_to_datetime)
@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@deserialize.parser("cycled_at", iso_to_datetime)
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
    payable_with: str
    active: bool
    expires_at: Optional[datetime.datetime]
    subitems: Optional[List[SubItemModel]]
    custom_variables: Optional[List[CustomVariableModel]]
    recent_invoices: Optional[List[RecentInvoiceModel]]
    suspend_on_invoice_expired: Optional[bool]
    two_step: Optional[bool]
    cycles_count: Optional[int]
    max_cycles: Optional[int]
    cycled_at: Optional[datetime.datetime]


@dataclass
class SubItemModel:
    id: str
    description: str
    quantity: int
    price_cents: int
    price: str
    total: str
    recurrent: bool


@deserialize.parser("due_date", iso_to_datetime)
@dataclass
class RecentInvoiceModel:
    id: str
    due_date: datetime.datetime
    status: str
    total: str
    secure_url: str


@deserialize.key("total_items", "totalItems")
@dataclass
class SubscriptionsModel:
    total_items: int
    items: List[SubscriptionModel]
