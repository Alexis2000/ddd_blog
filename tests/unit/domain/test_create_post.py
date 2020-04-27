from blog.domain.post import Post
from blog.domain.user import User
from blog.domain.post_error import PostError
from datetime import date
import pytest


def test_an_admin_can_create_a_post():
    admin = User('some-user-id', 'some-first-name', 'some-last-name', 'admin', date.today())
    post = Post('some-post-id', 'some-title', 'some-body', admin, date.today())

    assert post.author.id == 'some-user-id'


def test_a_none_admin_user_cannot_create_a_post():
    with pytest.raises(PostError):
        user = User('some-user-id', 'some-first-name', 'some-last-name', 'user', date.today())
        post = Post('some-post-id', 'some-title', 'some-body', user, date.today())

