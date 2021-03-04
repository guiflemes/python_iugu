import datetime
from typing import Dict, Any, Generic, TypeVar, Union, Match
from enum import Enum
import re

T = TypeVar("T")


def iso_to_datetime(date: Union[None, str]) -> Union[None, datetime.datetime]:
    if date is None:
        return None
    return _iso_to_datetime(date)


def _iso_to_datetime(iso_date: str) -> datetime.datetime:
    try:
        return datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S%z")
    except Exception:  # noqa
        return datetime.datetime.strptime(iso_date, "%Y-%m-%d")


def others_date_fmt(date: str) -> datetime.datetime:
    c = _ConvertDate(date)
    return c.convert_date()


class _ConvertDate:
    YEAR = datetime.datetime.now().year

    def __init__(self, date: str) -> None:
        self.date = date

    def find_pattern(self) -> Match:
        """pattern -> 11/02, 16:20"""
        fmt = "(0[1-9]|[12][0-9]|3[01])[/](0[1-9]|1[012])[,] ([01][0-9]|2[0-3]):([0-5][0-9])"
        regex = re.compile(fmt)
        match = regex.match(self.date)
        return match

    def convert_date(self) -> datetime.datetime:
        match = self.find_pattern()

        if match:
            self.date = self._make_iso_fmt_date(match)

        return iso_to_datetime(self.date)

    def _make_iso_fmt_date(self, match: Match) -> str:
        """date_fmt -> 2013-11-19T11:24:29-02:00"""

        date_fmt = "{}-{}-{}T{}:{}:00-00:00"
        date_iso = date_fmt.format(
            self.YEAR,
            match.group(2),  # -> month
            match.group(1),  # -> day
            match.group(3),  # -> hour
            match.group(4)  # -> minute
        )
        return date_iso


def to_dict(obj: Generic[T]) -> Dict[str, Any]:
    """
    This serialize python Object to Dict and remove None values
    :param obj: Any Python Object that respect __dict__ protocol
    :return:
    """
    if not hasattr(obj, "__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_") or val is None:
            continue

        if isinstance(val, Enum):
            val = val.value

        element = []
        if isinstance(val, list):
            for item in val:
                element.append(to_dict(item))
        else:
            element = to_dict(val)
        result[key] = element

    return result
