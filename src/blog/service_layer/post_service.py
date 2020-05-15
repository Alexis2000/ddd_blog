from blog.domain.post import Post
from datetime import date
from blog.adapters.post_abstract_unit_of_work import PostAbstractUnitOfWork
import uuid


def add_post(title: str, body: str, user_id: str, post_uow: PostAbstractUnitOfWork):
    with post_uow:
        user = post_uow.users.get(user_id)
        post_id = str(uuid.uuid4())
        post_uow.posts.add(Post(post_id, title, body, user, date.today()))
        post_uow.commit()

    return post_id
