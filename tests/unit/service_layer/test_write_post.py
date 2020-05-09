from datetime import date
from blog.domain.user import User
from blog.service_layer import services
from tests.unit.service_layer.fake_session import FakeSession
from tests.unit.service_layer.fake_post_repository import FakePostRepository


def test_add_post():
    repo, session = FakePostRepository([]), FakeSession()
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    post_id = services.add_post("Catchy Title", "some-text-body", admin, repo, session)
    assert post_id == repo.get(post_id).id


def test_commits():
    repo, session = FakePostRepository([]), FakeSession()
    session = FakeSession()
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    services.add_post("Catchy Title", "some-text-body", admin, repo, session)
    assert session.committed is True
