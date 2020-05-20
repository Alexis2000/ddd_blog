import abc
from blog.domain.entities.user import User


class UserAbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> User:
        raise NotImplementedError
