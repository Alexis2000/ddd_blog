from __future__ import annotations
import abc
from blog.adapters.abstract_repository import AbstractRepository


class UserAbstractUnitOfWork(abc.ABC):
    users: AbstractRepository

    def __enter__(self) -> UserAbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for user in self.users.seen:
            while user.events:
                yield user.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
