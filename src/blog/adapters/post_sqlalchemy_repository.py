from blog.adapters.abstract_repository import AbstractRepository
from blog.domain.entities.post import Post


class PostSqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def add(self, post):
        self.session.add(post)

    def get(self, post_id):
        return self.session.query(Post).filter_by(id=post_id).one()

    def list(self):
        return self.session.query(Post).all()
