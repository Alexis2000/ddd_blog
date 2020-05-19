from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from uuid import uuid4
from datetime import date
from blog import config
from blog.adapters import orm
from blog.service_layer import messagebus
from blog.service_layer.user_service import add_user
from blog.domain.events import PostCreated
from blog.adapters.post_sqlalchemy_unit_of_work import PostSqlAlchemyUnitOfWork
from blog.adapters.user_sqlalchemy_unit_of_work import UserSqlAlchemyUnitOfWork

orm.start_mappers()
get_session = sessionmaker(bind=create_engine(config.get_postgres_uri()))
app = Flask(__name__)


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    return "healthy", 200


@app.route("/user", methods=["POST"])
def create_user():
    request_data = request.get_json()
    uow = UserSqlAlchemyUnitOfWork()
    user_id = add_user(
        request_data["first_name"], request_data["last_name"], request_data["role"], uow
    )

    return jsonify({"user_id": user_id}), 201


@app.route("/add_post", methods=["POST"])
def create_post():
    request_data = request.get_json()
    post_id = messagebus.handle(
        PostCreated(
            str(uuid4()),
            request_data["admin_id"],
            request_data["title"],
            request_data["body"],
            date.today(),
        ),
        PostSqlAlchemyUnitOfWork(),
    ).pop(0)

    return jsonify({"post_id": post_id}), 201
