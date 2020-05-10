import uuid
import pytest
import requests
import datetime

from blog import config
from blog.domain.user import User


def create_user_request(first_name, last_name, role):
    url = config.get_api_url()
    return requests.post(
        f"{url}/user", json={"first_name": first_name, "last_name": last_name, "role": role}
    )


def post_to_add_post(title, body, admin_id):
    url = config.get_api_url()
    r = requests.post(
        f"{url}/add_post", json={"title": title, "body": body, "admin_id": admin_id}
    )
    assert r.status_code == 201


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_can_create_a_new_user():
    response = create_user_request('first-name', 'last-name', 'role-name')
    assert response.status_code == 201
    created_user_id = response.json()['user_id']
    assert uuid.UUID(created_user_id)


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_healthcheck():
    url = f"{config.get_api_url()}/healthcheck"
    r = requests.get(url)
    assert r.status_code == 200


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def can_post_a_new_log_post():
    user = User(str(uuid.uuid4()), "Testy", "Tester", "user", datetime.datetime.now())
    # TODO: Create a users SQLAlchemy Repo and persist the user as a fixture, then add the post for the user
    post_to_add_post("Some Title", "Some Body", user.id)
