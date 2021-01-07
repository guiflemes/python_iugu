import aiohttp
import asyncio

from expcetion import RequestsError
from iclient import IClient
from utils import to_dict
from version import __version__
from typing import Dict, Any, Generic, TypeVar
import os

T = TypeVar('T')


class _Client(IClient):
    _URL = "https://api.iugu.com/v1"

    def __init__(self, token: str) -> None:
        self._token = token

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, token: str) -> None:
        """
        it allows to change the token in runtime.
        Ex.: (prod to test)
        :param token:
        :return:
        """
        self._token = token

    @staticmethod
    def headers() -> Dict[str, str]:
        return {
            "User-Agent": "Async Iugu Python Api %s" % __version__,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    async def __request(self, session: aiohttp.ClientSession,
                        method: str, suffix: str, obj: Generic[T]) -> Dict[str, Any]:
        url = "%s/%s" % (self._URL, suffix)

        async with session.request(method, url, json=to_dict(obj)) as response:
            r = await response.json()

            if response.status == 200:
                return r

            raise RequestsError(r)

    async def _request(self, method: str, suffix: str, obj: Generic[T]) -> Dict[str, Any]:
        async with aiohttp.ClientSession(
                auth=aiohttp.BasicAuth(self.token, ""), headers=self.headers()) as session:
            response = await self.__request(session, method, suffix, obj)
            return response

    def _loop(self, method: str, suffix: str, obj: Generic[T] = None) -> Dict[str, Any]:
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(self._request(method, suffix, obj))
        return r

    def get(self, suffix: str, obj: Generic[T] = None) -> Dict[str, Any]:
        return self._loop('GET', suffix, obj)

    def post(self, suffix: str, obj: Generic[T] = None) -> Dict[str, Any]:
        return self._loop('POST', suffix, obj)

    def put(self, suffix: str, obj: Generic[T] = None) -> Dict[str, Any]:
        return self._loop('PUT', suffix, obj)

    def delete(self, suffix: str) -> Dict[str, Any]:
        return self._loop('DELETE', suffix)


__default_api__ = None


def default_api():
    global __default_api__
    if __default_api__ is None:
        try:
            token = os.environ["IUGU_API_TOKEN"]
        except KeyError:
            raise NotImplementedError
        __default_api__ = _Client(token=token)
    return __default_api__


def config(token: str):
    global __default_api__
    __default_api__ = _Client(token)
    return __default_api__
