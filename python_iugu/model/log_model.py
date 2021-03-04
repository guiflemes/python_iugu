from __future__ import annotations
from dataclasses import dataclass
import deserialize
from python_iugu.utils import log_date
import datetime


@deserialize.parser("created_at", log_date)
@dataclass
class LogModel:
    id: str
    description: str
    notes: str
    created_at: datetime.datetime
