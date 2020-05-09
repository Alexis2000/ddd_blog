from blog.domain.post import Post
from blog.domain.post import User
from uuid import uuid4
from datetime import datetime
from blog.adapters.post_sqlalchemy_repository import PostSqlAlchemyRepository


def test_repo_can_store_a_post_with_user(session):
    user = User(
        str(uuid4()),
        'Horst',
        'Seehofer',
        'admin',
        datetime.now()
    )
    user_id = user.id

    post = Post(
        str(uuid4()),
        'A Title',
        'A Body',
        user,
        datetime.now()
    )
    post_id = post.id

    repo = PostSqlAlchemyRepository(session)
    repo.add(post)
    session.commit()

    post_from_db = repo.get(post_id)
    assert post_from_db.id == post_id
    assert post_from_db._author.id == user_id
