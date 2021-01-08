from dataclasses import dataclass


@dataclass
class CustomVariable:
    name: str
    value: str
    _destroy: bool = False
