from blog.domain.entities.post import Post
from blog.adapters.post_abstract_unit_of_work import PostAbstractUnitOfWork
from blog.domain import events


def add_post(event: events.PostCreated, uow: PostAbstractUnitOfWork):
    with uow:
        user = uow.users.get(event.user_id)
        uow.posts.add(
            Post(event.post_id, event.title, event.body, user, event.created_at)
        )
        uow.commit()

    return event.post_id
