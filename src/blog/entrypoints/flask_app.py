from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from blog import config
from blog.adapters import orm
from blog.service_layer.post_service import add_post
from blog.service_layer.user_service import add_user
from blog.adapters.post_sqlalchemy_repository import PostSqlAlchemyRepository
from blog.adapters.post_sqlalchemy_unit_of_work import PostSqlAlchemyUnitOfWork

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return "healthy", 200


@app.route("/user", methods=["POST"])
def create_user():
    session = get_session()
    repo = PostSqlAlchemyRepository(session)
    request_data = request.get_json()
    user_id = add_user(
        request_data["first_name"],
        request_data["last_name"],
        request_data["role"],
        repo,
        session,
    )

    return jsonify({"user_id": user_id}), 201


@app.route("/add_post", methods=["POST"])
def create_post():
    request_data = request.get_json()

    title = request_data["title"]
    body = request_data["body"]
    author_id = request_data["admin_id"]

    uow = PostSqlAlchemyUnitOfWork()
    post_id = add_post(title, body, author_id, uow)

    return jsonify({"post_id": post_id}), 201
