# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from blog import config
from blog.adapters import post_abstract_repository
from blog.adapters.post_sqlalchemy_repository import PostSqlAlchemyRepository
from blog.adapters.post_abstract_unit_of_work import PostAbstractUnitOfWork


DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(config.get_postgres_uri(),))


class PostSqlAlchemyUnitOfWork(PostAbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.posts = PostSqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
