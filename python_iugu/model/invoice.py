from __future__ import annotations
from dataclasses import dataclass
import datetime
import deserialize
from python_iugu.model.custom_variable import CustomVariable
from python_iugu.model.item import Item
from python_iugu.utils import iso_to_datetime
from typing import List, Optional


@deserialize.parser("financial_return_date", iso_to_datetime)
@deserialize.parser("created_at_iso", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@deserialize.parser("authorized_at_iso", iso_to_datetime)
@deserialize.parser("expired_at_iso", iso_to_datetime)
@deserialize.parser("refunded_at_iso", iso_to_datetime)
@deserialize.parser("canceled_at_iso", iso_to_datetime)
@deserialize.parser("protested_at_iso", iso_to_datetime)
@deserialize.parser("chargeback_at_iso", iso_to_datetime)
@deserialize.parser("occurrence_date", iso_to_datetime)
@deserialize.parser("credit_card_captured_at", iso_to_datetime)
@dataclass
class Invoice:
    id: str
    due_date: str
    currency: str
    discount_cents: Optional[int]
    email: str
    items_total_cents: Optional[int]
    notification_url: Optional[str]
    return_url: Optional[str]
    status: str
    total_cents: Optional[int]
    total_paid_cents: Optional[int]
    taxes_paid_cents: Optional[int]
    paid_at: Optional[str]
    paid_cents: Optional[int]
    cc_emails: Optional[str]
    financial_return_date: Optional[datetime.datetime]
    payable_with: str
    ignore_canceled_email: Optional[bool]
    commission_cents: Optional[int]
    early_payment_discount: bool
    updated_at: datetime.datetime
    credit_card_brand: Optional[str]
    credit_card_bin: Optional[int]
    credit_card_last_4: Optional[str]
    credit_card_captured_at: Optional[datetime.datetime]
    credit_card_tid: Optional[str]
    payer_name: str
    payer_email: str
    payer_cpf_cnpj: Optional[str]
    payer_phone: Optional[str]
    payer_phone_prefix: Optional[str]
    payer_address_zip_code: Optional[str]
    payer_address_street: Optional[str]
    payer_address_district: Optional[str]
    payer_address_city: Optional[str]
    payer_address_state: Optional[str]
    payer_address_number: Optional[str]
    payer_address_complement: Optional[str]
    payer_address_country: Optional[str]
    secure_id: str
    secure_url: str
    customer_id: Optional[str]
    customer_ref: Optional[str]
    customer_name: Optional[str]
    user_id: Optional[str]
    total: Optional[str]
    taxes_paid: Optional[str]
    total_paid: Optional[str]
    total_overpaid: Optional[str]
    total_refunded: Optional[str]
    commission: Optional[str]
    fines_on_occurrence_day: Optional[str]
    total_on_occurrence_day: Optional[str]
    fines_on_occurrence_day_cents: Optional[int]
    total_on_occurrence_day_cents: Optional[int]
    refunded_cents: Optional[int]
    remaining_captured_cents: Optional[int]
    paid: str
    created_at_iso: datetime.datetime
    authorized_at_iso: Optional[datetime.datetime]
    expired_at_iso: Optional[datetime.datetime]
    refunded_at_iso: Optional[datetime.datetime]
    canceled_at_iso: Optional[datetime.datetime]
    protested_at_iso: Optional[datetime.datetime]
    chargeback_at_iso: Optional[datetime.datetime]
    occurrence_date: Optional[datetime.datetime]
    refundable: Optional[bool]
    installments: Optional[int]
    secure_id: Optional[str]
    payment_method: Optional[str]
    financial_return_dates: Optional[List[FinancialReturn]]
    items: Optional[List[Item]]
    custom_variables: Optional[List[CustomVariable]]


@deserialize.parser("return_date", iso_to_datetime)
@deserialize.parser("executed_date", iso_to_datetime)
@dataclass
class FinancialReturn:
    id: int
    installment: int
    return_date: datetime.datetime
    status: str
    amount: str
    taxes: str
    advanced: bool
    executed_date: Optional[datetime.datetime]
    commission: str


@deserialize.key("total_items", "totalItems")
@dataclass
class Invoices:
    total_items: int
    items: List[Invoice]
