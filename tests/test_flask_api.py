import pytest
import unittest
import json


from api import app as flask_app


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()


def test_status(client):
    response = client.get('/status')

    # Validate status code & content
    assert response.status_code == 200
    expected = {'status': 'Alive!'}
    assert expected == json.loads(response.get_data(as_text=True))

def test_login_no_body(client):
    response = client.post('/login')

    # Validate status code.
    assert response.status_code == 400

def test_login_no_username(client):
    payload = json.dumps({'password': '1234567'})
    
    response = client.post('/login',
                           data=payload,
                           content_type='application/json')

    # Validate status code.
    assert response.status_code == 400

def test_login_no_password(client):
    payload = json.dumps({"username": "dustybot"})

    response = client.post('/login',
                            data=payload,
                            content_type='application/json')

    # Validate status code & content
    assert response.status_code == 400

def test_login(client):
    payload = json.dumps({"username": "dustybot", "password": "1234567"})

    response = client.post('/login',
                            data=payload,
                            content_type='application/json')   
    # Validate status code.
    assert response.status_code == 200
    expected = {'status': "Login success for user dustybot with password of length: 7!!"}
    assert expected == json.loads(response.get_data(as_text=True))

def test_predict(client):
        url = "http://localhost:5000/predict/123/december/4"
        response = client.get('/predict/123/december/4')

        # Validate status code & content.
        assert response.status_code == 200
        assert 2000 <= int(json.loads(response.get_data(as_text=True))['prediction']) <= 5000