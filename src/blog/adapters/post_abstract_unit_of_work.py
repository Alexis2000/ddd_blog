from __future__ import annotations
import abc
from blog.adapters.post_abstract_repository import PostAbstractRepository
from blog.adapters.user_abstract_repository import UserAbstractRepository


class PostAbstractUnitOfWork(abc.ABC):
    posts: PostAbstractRepository
    users: UserAbstractRepository

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
