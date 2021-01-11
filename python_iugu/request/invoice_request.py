from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List
from python_iugu.request.utils_request import CustomVariableRequest


@dataclass
class InvoiceRequest:
    email: str
    payer: PayerRequest
    due_date: str  # fmt -> YYYY-MM-DD
    items: List[ItemRequest]
    cc_emails: Optional[str] = None
    return_url: Optional[str] = None
    notification_url: Optional[str] = None
    ignore_canceled_email: Optional[bool] = None
    fines: Optional[bool] = None
    late_payment_fine: Optional[int] = None
    per_day_interest: Optional[bool] = None
    per_day_interest_value: Optional[int] = None
    discount_cents: Optional[int] = None
    customer_id: Optional[str] = None
    ignore_due_email: Optional[bool] = None
    subscription_id: Optional[str] = None
    payable_with: Optional[str] = None
    credits: Optional[int] = None
    custom_variables: Optional[List[CustomVariableRequest]] = None
    early_payment_discount: Optional[int] = None
    early_payment_discounts: Optional[List[EarlyPaymentDiscountRequest]] = None
    external_reference: Optional[str] = None
    max_installments_value: Optional[int] = None
    ensure_workday_due_date: Optional[int] = None


@dataclass
class PayerRequest:
    cpf_cnpj: str
    name: str
    phone_prefix: str
    phone: str
    email: str
    address: AddressRequest


@dataclass
class AddressRequest:
    zip_code: str
    street: str
    number: str
    district: str
    city: str
    state: str
    country: str
    complement: Optional[str] = None


@dataclass
class EarlyPaymentDiscountRequest:
    days: int
    percent: float
    value_cents: int


@dataclass
class ItemRequest:
    description: str
    quantity: int
    price_cents: int
