from datetime import date
from blog.adapters import repository
from blog.domain.user import User
from blog.service_layer import services


class FakeRepository(repository.AbstractRepository):

    def __init__(self, posts):
        self._posts = set(posts)

    def add(self, post):
        self._posts.add(post)

    def get(self, id):
        return next(p for p in self._posts if p.id == id)

    def list(self):
        return list(self._posts)


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_add_post():
    repo, session = FakeRepository([]), FakeSession()
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    post_id = services.add_post("Catchy Title", "some-text-body", admin, repo, session)
    assert post_id == repo.get(post_id).id


def test_commits():
    repo, session = FakeRepository([]), FakeSession()
    session = FakeSession()
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    services.add_post("Catchy Title", "some-text-body", admin, repo, session)
    assert session.committed is True
