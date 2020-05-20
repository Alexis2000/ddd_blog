from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from blog import config
from blog.adapters.user_sqlalchemy_repository import UserSqlAlchemyRepository
from blog.adapters.user_abstract_unit_of_work import UserAbstractUnitOfWork


DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(config.get_postgres_uri(),))


class UserSqlAlchemyUnitOfWork(UserAbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.users = UserSqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
