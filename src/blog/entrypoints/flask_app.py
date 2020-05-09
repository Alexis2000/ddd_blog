from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from blog import config
from blog.adapters import orm
from blog.service_layer import services

from blog.adapters.post_sqlalchemy_repository import PostSqlAlchemyRepository

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)


@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return 'healthy', 200


@app.route("/add_post", methods=['POST'])
def add_batch():
    session = get_session()
    repo = PostSqlAlchemyRepository(session)

    request_data = request.get_json()

    title = request_data['title']
    body = request_data['body']
    author_id = request_data['author_id']

    services.add_post(
        title, body, author_id, repo, session
    )

    return 'OK', 201


