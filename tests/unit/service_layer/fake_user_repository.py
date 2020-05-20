from blog.adapters.abstract_repository import AbstractRepository


class FakeUserRepository(AbstractRepository):
    def __init__(self, users):
        super().__init__()
        self._users = set(users)

    def add(self, user):
        self._users.add(user)

    def get(self, id):
        return next(u for u in self._users if u.id == id)

    def list(self):
        return list(self._users)
