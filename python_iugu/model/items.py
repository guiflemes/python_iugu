from dataclasses import dataclass
import deserialize
from python_iugu.utils import iso_to_datetime
import datetime


@deserialize.parser("created_at", iso_to_datetime)
@deserialize.parser("updated_at", iso_to_datetime)
@dataclass
class Item:
    id: str
    description: str
    price_cents: int
    quantity: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
