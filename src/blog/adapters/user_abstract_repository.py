import abc
from blog.domain.user import User


class UserAbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id) -> User:
        raise NotImplementedError
