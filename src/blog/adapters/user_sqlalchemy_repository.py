from blog.adapters.abstract_repository import AbstractRepository
from blog.domain.entities.user import User


class UserSqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def add(self, user):
        self.session.add(user)

    def get(self, user_id):
        return self.session.query(User).filter_by(id=user_id).one()

    def list(self):
        return self.session.query(User).all()
