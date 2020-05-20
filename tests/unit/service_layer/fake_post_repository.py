from blog.adapters.abstract_repository import AbstractRepository


class FakePostRepository(AbstractRepository):
    def __init__(self, posts):
        super().__init__()
        self._posts = set(posts)

    def add(self, post):
        self._posts.add(post)

    def get(self, id):
        return next(p for p in self._posts if p.id == id)

    def list(self):
        return list(self._posts)
