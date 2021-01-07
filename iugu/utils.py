import datetime
from typing import Dict, Any, Generic, TypeVar, Union

T = TypeVar("T")


def iso_to_datetime(date: Union[None, str]) -> Union[None, datetime.datetime]:
    if date is None:
        return None

    return _iso_to_datetime(date)


def _iso_to_datetime(iso_date: str) -> datetime.datetime:
    try:
        return datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S%z")
    except Exception as err:
        return datetime.datetime.strptime(iso_date, "%Y-%m-%d")


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
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(to_dict(item))
        else:
            element = to_dict(val)
        result[key] = element
    return result
