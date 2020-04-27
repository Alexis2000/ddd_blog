from datetime import date
from blog.domain.user import User
from blog.domain.post_error import PostError


class Post:
    def __init__(self, post_id: str, title: str, body: str, author: User, created_at: date):
        if author.role != 'admin':
            raise PostError('The author must be an admin')
        self.post_id = post_id
        self.title = title
        self.body = body
        self.author = author
        self.created_at = created_at
