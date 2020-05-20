from blog.domain.entities.user import User
from blog.adapters.user_abstract_unit_of_work import UserAbstractUnitOfWork
from blog.domain.events.UserCreated import UserCreated


def add_user(event: UserCreated, uow: UserAbstractUnitOfWork):
    with uow:
        uow.users.add(
            User(
                event.user_id,
                event.first_name,
                event.last_name,
                event.role,
                event.created_at,
            )
        )
        uow.commit()

    return event.user_id
