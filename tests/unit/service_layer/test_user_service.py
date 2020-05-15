from datetime import date
from blog.domain.user import User

from tests.unit.service_layer.fake_user_unit_of_work import FakeUserUnitOfWork


def test_add_user_with_unit_of_work():
    uow = FakeUserUnitOfWork()
    uow.users.add(
        User("some-user-id", "some-first-name", "some-last-name", "admin", date.today())
    )
    uow.commit()
    user = uow.users.get('some-user-id')
    assert user.first_name == "some-first-name"

