from datetime import date
from blog.domain.entities.user import User
from blog.domain.events.PostCreated import PostCreated
from blog.service_layer import messagebus

from tests.unit.service_layer.fake_post_unit_of_work import FakePostUnitOfWork


def test_add_post_by_putting_event_on_message_bus():
    uow = FakePostUnitOfWork()
    uow.users.add(
        User("some-user-id", "some-first-name", "some-last-name", "admin", date.today())
    )
    uow.commit()

    messagebus.handle(
        event=PostCreated(
            "post-id123", "some-user-id", "some-title", "some-body", "22-2-1997"
        ),
        uow=uow,
    )
    assert uow.committed
    post = uow.posts.get("post-id123")
    assert "post-id123" == post.id
    assert post.title == "some-title"
    assert post.body == "some-body"
    assert post._author.id == "some-user-id"
