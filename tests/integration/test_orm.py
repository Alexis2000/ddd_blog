from blog.domain.post import Post
from blog.domain.post import User
from sqlalchemy.orm import joinedload
from datetime import date


def test_post_mapper_can_load_posts(session):
    session.execute(
        'INSERT INTO posts (id, title, body, author, created_at) VALUES '
        '("post1", "Title", "Body", "author1", "2011-04-11"),'
        '("post2", "Title", "Body", "author1", "2011-04-11"),'
        '("post3", "Title", "Body", "author1", "2011-04-12")'
    )
    session.execute(
        'INSERT INTO users (id, first_name, last_name, role, created_at) VALUES '
        '("author1", "Jon", "Doe", "admin", "2011-04-11")'
    )
    expected = [
        Post("post1", "Title", "Body", "author1", "2011-04-11"),
        Post("post2", "Title", "Body", "author1", "2011-04-11"),
        Post("post3", "Title", "Body", "author1", "2011-04-12"),
    ]
    assert session.query(Post).all() == expected


def test_mapper_can_load_users(session):
    session.execute(
        'INSERT INTO users (id, first_name, last_name, role, created_at) VALUES '
        '("user1", "Jon", "Doe", "admin", "2011-04-11"),'
        '("user2", "Tom", "Jones", "admin", "2011-04-11"),'
        '("user3", "Hannah", "Brown", "user", "2011-04-11")'
    )
    expected = [
        User("user1", "Jon", "Doe", "admin", "2011-04-11"),
        User("user2", "Tom", "Jones", "admin", "2011-04-11"),
        User("user3", "Hannah", "Brown", "user", "2011-04-11"),
    ]
    assert session.query(User).all() == expected


def test_mapper_can_load_posts_with_author(session):
    session.execute(
        'INSERT INTO users (id, first_name, last_name, role, created_at) VALUES '
        '("user1", "Jon", "Doe", "admin", "2011-04-11")'
    )
    session.execute(
        'INSERT INTO posts (id, title, body, author, created_at) VALUES '
        '("post1", "Title", "Body", "user1", "2011-04-11")'
    )
    post = session.query(Post).filter_by(id='post1').first()
    assert post.author == "user1"
    assert post._author.id == "user1"
