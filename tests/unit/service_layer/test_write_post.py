import pytest
from datetime import date
from blog.adapters import repository
from blog.domain.user import User
from blog.service_layer import services


class FakeRepository(repository.AbstractRepository):

    def __init__(self, posts):
        self._posts = set(posts)

    def add(self, post):
        self._posts.add(post)

    def get(self, post_id):
        return next(p for p in self._posts if p.post_id == post_id)

    def list(self):
        return list(self._posts)


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


def test_add_post():
    repo, session = FakeRepository([]), FakeSession()
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    post_id = services.add_post("some_id", "Catchy Title", "some-text-body", admin, date.today(), repo, session)
    assert repo.get("some_id").post_id == "some_id"
    assert post_id == repo.get("some_id").post_id


def test_commits():
    repo, session = FakeRepository([]), FakeSession()
    session = FakeSession()
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    services.add_post("some_id", "Catchy Title", "some-text-body", admin, date.today(), repo, session)
    assert session.committed is True
