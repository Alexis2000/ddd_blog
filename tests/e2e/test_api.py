import uuid
import pytest
import requests
import datetime

from blog import config
from blog.domain.user import User


@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_healthcheck():
    url = f'{config.get_api_url()}/healthcheck'
    r = requests.get(url)
    assert r.status_code == 200


def post_to_add_post(title, body, admin_id):
    url = config.get_api_url()
    r = requests.post(
        f'{url}/add_post',
        json={'title': title, 'body': body, 'admin_id': admin_id}
    )
    assert r.status_code == 201


@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def can_post_a_new_log_post():
    user = User(str(uuid.uuid4()), 'Testy', 'Tester', 'user', datetime.datetime.now())
    # TODO: Create a users SQLAlchemy Repo and persist the user as a fixture, then add the post for the user
    post_to_add_post(
        'Some Title',
        'Some Body',
        user.id
    )
