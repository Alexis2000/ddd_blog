from datetime import date
from sqlalchemy.orm import mapper, relationship, clear_mappers, sessionmaker, Session
from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date,
    ForeignKey, create_engine
)

# Experimental script

class User:
    def __init__(self, user_id: str, first_name: str, last_name: str, role: str, created_at: date):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.created_at = created_at

    def __repr__(self):
        return f'<User {self.id}>'

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)


class Post:

    def __init__(self, post_id: str, title: str, body: str, user: User, created_at: date):
        self.id = post_id
        self.title = title
        self.body = body
        self._author = user
        self.created_at = created_at

    def __repr__(self):
        return f'<Post {self.id}>'

    def __eq__(self, other):
        if not isinstance(other, Post):
            return False
        return other.id == self.id

    def __hash__(self):
        return hash(self.id)


engine = create_engine("sqlite:///some.db")
session = Session(bind=engine)
metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', String(255), primary_key=True, autoincrement=False),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('role', String(255)),
    Column('created_at', Date, nullable=False),
)

posts = Table(
    'posts', metadata,
    Column('id', String(255), primary_key=True, autoincrement=False),
    Column('title', String(255)),
    Column('body', String(255)),
    Column('author', ForeignKey('users.id')),
    Column('created_at', Date, nullable=False),
)

mapper(Post, posts, properties={
    '_author': relationship(User, backref='posts')
})
mapper(User, users, properties={
    'user': relationship(Post, back_populates="_author")
})

user = User(
    '1234600',
    'Lucas',
    'Hirsch',
    'admin',
    date.today()
)

post = Post(
    '12345700',
    'some-title',
    'some-body',
    user,
    date.today()
)

post._author = user

# create the tables
# users.create(engine)
# posts.create(engine)

# persist the user and the post
# session.add(user)
# session.add(post)
# session.commit()

# query for the post with the user
post = session.query(Post).filter_by(id='12345700').one()._author.first_name
print(post)

