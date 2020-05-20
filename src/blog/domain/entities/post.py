from datetime import date
from blog.domain.entities.user import User
from blog.domain.post_error import PostError


class Post:
    def __init__(
        self, post_id: str, title: str, body: str, user: User, created_at: date
    ):
        if user.role != "admin":
            raise PostError("The author must have the role admin")
        self.id = post_id
        self.title = title
        self.body = body
        self._author = user
        self.created_at = created_at

    def __repr__(self):
        return f"<Post {self.id}>"

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)
