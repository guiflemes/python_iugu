import abc


class IClient(abc.ABC):

    @abc.abstractmethod
    def get(self, suffix: str, obj: object):
        pass

    @abc.abstractmethod
    def post(self, url: str, obj: object):
        pass

    @abc.abstractmethod
    def put(self, url: str, obj: object):
        pass

    @abc.abstractmethod
    def delete(self, url: str):
        pass
