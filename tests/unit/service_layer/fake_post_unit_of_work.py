from blog.adapters.post_abstract_unit_of_work import PostAbstractUnitOfWork
from fake_post_repository import FakePostRepository
from fake_user_repository import FakeUserRepository


class FakePostUnitOfWork(PostAbstractUnitOfWork):
    def __init__(self):
        self.posts = FakePostRepository([])
        self.users = FakeUserRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass
