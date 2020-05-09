from blog.adapters.user_abstract_repository import UserAbstractRepository


class FakeUserRepository(UserAbstractRepository):

    def __init__(self, users):
        self._users = set(users)

    def add(self, user):
        self._users.add(user)

    def get(self, id):
        return next(u for u in self._users if u.id == id)

    def list(self):
        return list(self._users)
