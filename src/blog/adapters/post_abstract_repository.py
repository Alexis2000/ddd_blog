import abc
from blog.domain.post import Post


class PostAbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    @abc.abstractmethod
    def add(self, batch: Post):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Post:
        raise NotImplementedError
