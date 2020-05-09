from blog.domain.post import Post
from blog.adapters.post_abstract_repository import PostAbstractRepository
from blog.adapters.user_abstract_repository import UserAbstractRepository
from blog.domain.user import User
from datetime import date
import uuid


def add_post(
    title: str,
    body: str,
    user_id: str,
    posts_repo: PostAbstractRepository,
    users_repo: UserAbstractRepository,
    session,
):
    author = users_repo.get(user_id)
    post_id = str(uuid.uuid4())
    posts_repo.add(Post(post_id, title, body, author, date.today()))
    session.commit()

    return post_id
