from python_iugu.client import default_api, IClient
from typing import Optional, Dict, Any, Generic, TypeVar
import deserialize

T = TypeVar('T')


class BaseService:

    def __init__(self, client: Optional[IClient] = None) -> None:
        if client is None:
            client = default_api()
        self.client = client

    @staticmethod
    def _deserialize(obj: Generic[T], data: Dict[str, Any]) -> Generic[T]:
        return deserialize.deserialize(obj, data)
