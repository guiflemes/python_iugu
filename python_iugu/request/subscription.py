from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

from .custom_variable import CustomVariableRequest


@dataclass
class SubscriptionRequest:
    customer_id: str
    plan_identifier: Optional[str] = None
    expires_at: Optional[str] = None  # fmt -> DD-MM-YYYY
    only_on_charge_success: Optional[bool] = None
    ignore_due_email: Optional[bool] = None
    payable_with: Optional[str] = None
    credits_based: Optional[bool] = None
    price_cents: Optional[int] = None
    credits_cycle: Optional[int] = None
    credits_min: Optional[int] = None
    subitems: Optional[List[SubItem]] = None
    custom_variables: Optional[List[CustomVariableRequest]] = None
    two_step: Optional[bool] = None
    suspend_on_invoice_expired: Optional[bool] = None
    only_charge_on_due_date: Optional[bool] = None


@dataclass
class SubItem:
    description: str
    price_cents: int
    quantity: int
    recurrent: bool
    id: Optional[str] = None
    _destroy: Optional[bool] = None
