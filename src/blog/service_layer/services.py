from blog.domain.post import Post
from blog.adapters.repository import AbstractRepository
from blog.domain.user import User
from datetime import date


def add_post(
        post_id: str, title: str, body: str, author: User, created_at: date,
        repo: AbstractRepository, session,
):
    repo.add(Post(post_id, title, body, author, created_at))
    session.commit()

    return post_id
