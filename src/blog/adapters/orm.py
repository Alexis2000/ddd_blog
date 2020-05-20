from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship
from blog.domain.entities.post import Post
from blog.domain.entities.user import User


metadata = MetaData()


users = Table(
    "users",
    metadata,
    Column("id", String(255), primary_key=True, autoincrement=False),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("role", String(255)),
    Column("created_at", Date, nullable=False),
)

posts = Table(
    "posts",
    metadata,
    Column("id", String(255), primary_key=True, autoincrement=False),
    Column("title", String(255)),
    Column("body", String(255)),
    Column("author", ForeignKey("users.id")),
    Column("created_at", Date, nullable=False),
)


def start_mappers():
    mapper(Post, posts, properties={"_author": relationship(User, backref="posts")})
    mapper(
        User, users, properties={"user": relationship(Post, back_populates="_author")}
    )
    pass
