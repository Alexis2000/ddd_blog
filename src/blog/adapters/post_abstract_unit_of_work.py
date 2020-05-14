from __future__ import annotations
import abc
from blog.adapters.post_abstract_repository import PostAbstractRepository


class PostAbstractUnitOfWork(abc.ABC):
    posts: PostAbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
