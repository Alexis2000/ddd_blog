from __future__ import annotations
import abc
from blog.adapters.abstract_repository import AbstractRepository


class PostAbstractUnitOfWork(abc.ABC):
    posts: AbstractRepository
    users: AbstractRepository

    def __enter__(self) -> PostAbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for post in self.posts.seen:
            while post.events:
                yield post.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
