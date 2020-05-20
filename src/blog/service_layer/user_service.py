from blog.adapters.user_abstract_unit_of_work import UserAbstractUnitOfWork
from blog.domain.entities.user import User
from sqlalchemy.sql import func
import uuid


def add_user(
    first_name: str, last_name: str, role: str, user_uow: UserAbstractUnitOfWork
):
    with user_uow:
        user_id = str(uuid.uuid4())
        user_uow.users.add(User(user_id, first_name, last_name, role, func.now()))
        user_uow.commit()

    return user_id
