from datetime import date
from blog.domain.user import User
from blog.service_layer.post_service import add_post

from tests.unit.service_layer.fake_post_unit_of_work import FakePostUnitOfWork


def test_add_post_with_unit_of_work():
    uow = FakePostUnitOfWork()
    uow.users.add(
        User("some-user-id", "some-first-name", "some-last-name", "admin", date.today())
    )
    uow.commit()

    post_id = add_post("special-title", "cool-body", "some-user-id", uow)
    post = uow.posts.get(post_id)
    assert post_id == post.id
