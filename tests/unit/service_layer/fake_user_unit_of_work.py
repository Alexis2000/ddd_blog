from blog.adapters.user_abstract_unit_of_work import UserAbstractUnitOfWork
from fake_user_repository import FakeUserRepository


class FakeUserUnitOfWork(UserAbstractUnitOfWork):
    def __init__(self):
        self.users = FakeUserRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass
