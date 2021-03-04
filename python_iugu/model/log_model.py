from __future__ import annotations
from dataclasses import dataclass
import deserialize
from python_iugu.utils import others_date_fmt
import datetime


@deserialize.parser("created_at", others_date_fmt)
@dataclass
class LogModel:
    id: str
    description: str
    notes: str
    created_at: datetime.datetime
