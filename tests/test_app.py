"""
test_app.py
This script tests the app.
"""

import os
import tempfile
import pytest
from app.app import create_app

app = create_app()


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


def test_get_fork(client):
    """
    Test HTTP GET to /fork.
    :return:
    """

    # Make the request.
    rv = client.get('/fork/')

    # Test no redirect.
    assert rv.status_code == 200


def do_fork(client, username, password):
    """
    Test a fork call.
    :param client:
    :param username:
    :param password:
    :return:
    """

    return client.post('/fork/', data={
        'username': username,
        'password': password
    })


def test_post_fork(client):
    """
    Test HTTP Post to /fork
    :param client:
    :return:
    """

    # Test a failed fork.
    rv = do_fork(client, '', '')
    assert rv.status_code == 200
    assert (b'Authentication error' in rv.data)
