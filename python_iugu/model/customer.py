from dataclasses import dataclass
import datetime
from typing import List, Optional
from python_iugu.utils import iso_to_datetime
from python_iugu.model.custom_variable import CustomVariable
import deserialize


@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@dataclass
class Customer:
    id: str
    email: str
    name: str
    notes: Optional[str]
    phone: Optional[str]
    phone_prefix: Optional[str]
    cpf_cnpj: Optional[str]
    cc_emails: Optional[str]
    zip_code: Optional[str]
    number: Optional[str]
    complement: Optional[str]
    city: Optional[str]
    state: Optional[str]
    district: Optional[str]
    street: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    custom_variables: Optional[List[CustomVariable]]


@deserialize.key("total_items", "totalItems")
@dataclass
class Customers:
    total_items: int
    items: List[Customer]
