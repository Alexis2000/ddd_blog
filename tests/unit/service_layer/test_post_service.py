from datetime import date
from blog.domain.entities.user import User
from blog.domain.events.PostCreated import PostCreated
from blog.domain.events.UserCreated import UserCreated
from blog.service_layer import messagebus
from uuid import uuid4

from tests.unit.service_layer.fake_post_unit_of_work import FakePostUnitOfWork


def test_add_post():

    uow = FakePostUnitOfWork()

    user_id = messagebus.handle(
        UserCreated(
            str(uuid4()),
            "first_name",
            "last_name",
            "admin",
            date.today(),
        ),
        uow,
    ).pop(0)

    post_id = messagebus.handle(
        PostCreated(
            str(uuid4()), user_id, "some-title", "some-body", "22-2-1997"
        ),
        uow,
    ).pop(0)

    assert uow.committed
    post = uow.posts.get(post_id)
    assert post_id == post.id
    assert post.title == "some-title"
    assert post.body == "some-body"
    assert post._author.id == user_id
