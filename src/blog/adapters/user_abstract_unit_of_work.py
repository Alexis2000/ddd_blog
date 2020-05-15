from __future__ import annotations
import abc
from blog.adapters.user_abstract_repository import UserAbstractRepository


class UserAbstractUnitOfWork(abc.ABC):
    users: UserAbstractRepository

    def __enter__(self) -> UserAbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
