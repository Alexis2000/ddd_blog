from blog.adapters.user_abstract_repository import UserAbstractRepository
from blog.domain.post import User


class PostSqlAlchemyRepository(UserAbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, user):
        self.session.add(User)

    def get(self, user_id):
        return self.session.query(User).filter_by(id=user_id).one()

    def list(self):
        return self.session.query(User).all()
