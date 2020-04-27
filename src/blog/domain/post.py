from datetime import date
from blog.domain.user import User
from blog.domain.post_error import PostError

class Post:
    def __init__(self, post_id: str, title: str, body: str, user: User, created_at: date):
        if user.role != 'admin':
            raise PostError('Author must be admin')
        self.id = post_id
        self.title = title
        self.body = body
        self.author = user
        self.created_at = created_at