import abc
from blog.domain.entities.post import Post


class PostAbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    @abc.abstractmethod
    def add(self, post: Post):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, post_id) -> Post:
        raise NotImplementedError
