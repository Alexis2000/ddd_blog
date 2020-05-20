import abc
from blog.domain.entities.entity import Entity


class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()

    @abc.abstractmethod
    def add(self, entity: Entity):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, entity_id) -> Entity:
        raise NotImplementedError
