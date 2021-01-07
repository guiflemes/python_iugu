from dataclasses import dataclass


@dataclass
class CustomVariableRequest:
    name: str
    value: str
    _destroy: bool = False
