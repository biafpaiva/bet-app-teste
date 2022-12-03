import pytest
from flask_backend import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.secret_key = 'super secret key'
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


def test_list_matches(client):
    resp = client.get('/list_matches')
    assert resp.status_code == 200

'''
def test_register_user(client):
    resp = client.post('/register_user', data={
        'username': 'engSoftware', 'password': 'unitTesting', 'email': 'unit@test.com'
    })
    assert resp.status_code == 200

def test_login_user(client):
    resp = client.post('/login_user', data={
        'email': 'admin@admin.com', 'password': 'eusouadm'
    })
    assert resp.status_code == 200

def test_user_data(client):
    resp = client.get('/user_data')
    assert resp.status_code == 200

'''
