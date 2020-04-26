import pytest


class FakeRepository(repository.AbstractRepository):

    def __init__(self, posts):
        self._posts = set(posts)

    def add(self, post):
        self._posts.add(post)

    def get(self, post_id):
        return next(p for p in self._posts if p.post_id == post_id)

    def list(self):
        return list(self._posts)


def test_add_post():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, repo, session)
    assert repo.get("b1") is not None
    assert session.committed
