from dataclasses import dataclass
from typing import Optional


@dataclass
class CustomVariableModel:
    name: str
    value: Optional[str]
