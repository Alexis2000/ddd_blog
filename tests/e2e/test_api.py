import uuid
import pytest
import requests

from blog import config


def post_to_add_post(title, body, admin_id):
    url = config.get_api_url()
    r = requests.post(
        f'{url}/add_post',
        json={'title': title, 'body': body, 'admin_id': admin_id}
    )
    assert r.status_code == 201


@pytest.mark.usefixtures('restart_api')
@pytest.mark.usefixtures('postgres_db')
def can_post_a_new_log_post():
    post_to_add_post(
        'Some Title',
        'Some Body',
        'admin-id'
    )