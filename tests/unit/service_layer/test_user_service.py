from datetime import date
from uuid import uuid4
import uuid
from blog.service_layer import messagebus
from tests.unit.service_layer.fake_user_unit_of_work import FakeUserUnitOfWork
from blog.domain.events.UserCreated import UserCreated


def test_add_user_with_domain_event():
    uow = FakeUserUnitOfWork()
    user_id = str(uuid4())
    user_created_event = UserCreated(
        user_id, "some-first-name", "some-last-name", "a-role", date.today()
    )
    messagebus.handle(event=user_created_event, uow=uow)

    assert uow.committed
    user = uow.users.get(user_id)
    assert uuid.UUID(user.id)
    assert user.id == user_id
    assert user.first_name == "some-first-name"
    assert user.last_name == "some-last-name"
    assert user.role == "a-role"
