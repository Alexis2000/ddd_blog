import uuid
import pytest
import requests

from blog import config


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_healthcheck():
    url = f"{config.get_api_url()}/healthcheck"
    assert requests.get(url).status_code == 200


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_can_create_a_new_user():
    response = create_user_request("first-name", "last-name", "role-name")
    assert response.status_code == 201
    created_user_id = response.json()["user_id"]
    assert uuid.UUID(created_user_id)


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_can_post_a_new_blog_post():
    user_response = create_user_request("first-name", "last-name", "admin")
    created_user_id = user_response.json()["user_id"]
    post_response = create_post_request("Some Title", "Some Body", created_user_id)
    post_id = post_response.json()["post_id"]
    assert uuid.UUID(post_id)


def create_user_request(first_name, last_name, role):
    url = config.get_api_url()
    return requests.post(
        f"{url}/user",
        json={"first_name": first_name, "last_name": last_name, "role": role},
    )


def create_post_request(title, body, admin_id):
    url = config.get_api_url()
    response = requests.post(
        f"{url}/add_post", json={"title": title, "body": body, "admin_id": admin_id}
    )
    assert response.status_code == 201

    return response
