from __future__ import annotations
import abc
from blog.adapters.post_abstract_repository import PostAbstractRepository
from blog.adapters.user_abstract_repository import UserAbstractRepository


class PostAbstractUnitOfWork(abc.ABC):
    posts: PostAbstractRepository
    users: UserAbstractRepository

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
