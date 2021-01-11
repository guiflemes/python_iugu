from dataclasses import dataclass
from typing import List, Optional
from python_iugu.request.utils_request import CustomVariableRequest


@dataclass
class CustomerRequest:
    email: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[str] = None
    phone: Optional[str] = None
    phone_prefix: Optional[str] = None
    cpf_cnpj: Optional[str] = None
    cc_emails: Optional[str] = None
    zip_code: Optional[str] = None
    number: Optional[str] = None
    complement: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    district: Optional[str] = None
    street: Optional[str] = None
    custom_variables: Optional[List[CustomVariableRequest]] = None
