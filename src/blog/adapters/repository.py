import abc
from blog.domain import Post

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, batch: model.Post):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Post:
        raise NotImplementedError