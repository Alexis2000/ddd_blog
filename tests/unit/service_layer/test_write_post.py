from datetime import date
from blog.domain.user import User
from blog.service_layer.post_service import add_post
from tests.unit.service_layer.fake_session import FakeSession
from tests.unit.service_layer.fake_post_repository import FakePostRepository
from tests.unit.service_layer.fake_user_repository import FakeUserRepository


def test_add_post():
    posts_repo, users_repo, session = (
        FakePostRepository([]),
        FakeUserRepository([]),
        FakeSession(),
    )
    users_repo.add(
        User("some-user-id", "some-first-name", "some-last-name", "admin", date.today())
    )
    post_id = add_post(
        "Catchy Title",
        "some-text-body",
        "some-user-id",
        posts_repo,
        users_repo,
        session,
    )
    assert session.committed is True
    assert post_id == posts_repo.get(post_id).id
