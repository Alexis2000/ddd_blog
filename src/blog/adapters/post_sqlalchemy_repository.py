from blog.adapters.repository import AbstractRepository
from blog.domain.post import Post


class PostSqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def add(self, post):
        self.session.add(post)

    def get(self, post_id):
        return self.session.query(Post).filter_by(id=post_id).one()

    def list(self):
        return self.session.query(Post).all()
