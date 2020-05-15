import pytest
from uuid import uuid4
from datetime import date
from blog.adapters.post_sqlalchemy_unit_of_work import PostSqlAlchemyUnitOfWork


def insert_user(
    session, user_id: str, first_name: str, last_name: str, role: str, created_at
):
    session.execute(
        "INSERT INTO users (id, first_name, last_name, role, created_at)"
        " VALUES (:id, :first_name, :last_name, :role, :created_at)",
        dict(
            id=user_id,
            first_name=first_name,
            last_name=last_name,
            role=role,
            created_at=created_at,
        ),
    )


def insert_a_post(
    session, post_id: str, title: str, body: str, author_id: str, created_at
):
    session.execute(
        "INSERT INTO posts (id, title, body, author, created_at)"
        " VALUES (:id, :title, :body, :author_id, :created_at)",
        dict(
            id=post_id,
            title=title,
            body=body,
            author_id=author_id,
            created_at=created_at,
        ),
    )


def test_unit_of_work_can_edit_a_post(session_factory):
    session = session_factory()
    user_id = str(uuid4())
    post_id = str(uuid4())
    insert_user(session, user_id, "some-f-name", "some-l-name", "admin", date.today())
    insert_a_post(session, post_id, "a-title", "a-body", user_id, date.today())
    session.commit()

    uow = PostSqlAlchemyUnitOfWork(session_factory)
    with uow:
        post = uow.posts.get(post_id)
        post.title = "changed-title"
        author = post._author
        author.first_name = "some-changed-name"
        uow.commit()

    post = uow.posts.get(post_id)
    assert post.title == "changed-title"
    assert post._author.first_name == "some-changed-name"


def test_rolls_back_uncommitted_work_by_default(session_factory):
    uow = PostSqlAlchemyUnitOfWork(session_factory)
    user_id = str(uuid4())
    post_id = str(uuid4())

    with uow:
        insert_user(
            uow.session, user_id, "some-f-name", "some-l-name", "admin", date.today()
        )
        insert_a_post(uow.session, post_id, "a-title", "a-body", user_id, date.today())

    new_session = session_factory()
    rows = list(new_session.execute('SELECT * FROM "posts"'))
    assert rows == []


def test_rolls_back_on_error(session_factory):
    class MyException(Exception):
        pass

    uow = PostSqlAlchemyUnitOfWork(session_factory)
    user_id = str(uuid4())
    post_id = str(uuid4())
    with pytest.raises(MyException):
        with uow:
            insert_user(
                uow.session,
                user_id,
                "some-f-name",
                "some-l-name",
                "admin",
                date.today(),
            )
            insert_a_post(
                uow.session, post_id, "a-title", "a-body", user_id, date.today()
            )
            raise MyException()

    new_session = session_factory()
    rows = list(new_session.execute('SELECT * FROM "posts"'))
    assert rows == []
    rows = list(new_session.execute('SELECT * FROM "users"'))
    assert rows == []
