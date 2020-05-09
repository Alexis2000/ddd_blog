from blog.domain.post import Post
from blog.adapters.post_abstract_repository import PostAbstractRepository
from blog.adapters.user_abstract_repository import UserAbstractRepository
from blog.domain.user import User
from sqlalchemy.sql import func
import datetime
import uuid


def add_user(
    first_name: str,
    last_name: str,
    role: str,
    users_repo: UserAbstractRepository,
    session
):
    user_id = str(uuid.uuid4())
    users_repo.add(User(
        user_id,
        first_name,
        last_name,
        role,
        func.now()
    ))

    session.commit()

    return user_id
