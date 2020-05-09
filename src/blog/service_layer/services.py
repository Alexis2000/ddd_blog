from blog.domain.post import Post
from blog.adapters.post_abstract_repository import PostAbstractRepository
from blog.domain.user import User
from datetime import date
import uuid


def add_post(
    title: str, body: str, author: User, repo: PostAbstractRepository, session,
):
    post_id = str(uuid.uuid4())
    repo.add(Post(post_id, title, body, author, date.today()))
    session.commit()

    return post_id
