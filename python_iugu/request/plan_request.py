from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from python_iugu import enuns


@dataclass
class PlanRequest:
    name: str = None
    identifier: str = None
    interval: int = None
    interval_type: enuns.IntervalType = None
    value_cents: int = None
    payable_with: enuns.PayableWith = None
    features: Optional[FeatureRequest] = None
    billing_days: int = None
    max_cycles: int = None


@dataclass
class FeatureRequest:
    name: str
    identifier: str
    value: str
