import abc
from blog.domain.post import Post


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, batch: Post):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Post:
        raise NotImplementedError
