from flask_boilerplate import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.data == b'Hello World!'

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello World!'

    response = client.get('/hello?name=Jim')
    assert response.data == b'Hello Jim!'


def test_number(client):
    response = client.get('/number/1')
    assert response.data == b"Number: 1"

    response = client.get('/number/2')
    assert response.data == b"Number: 2"

    response = client.get('/number/apple')
    assert response.status_code == 404
# This was the code to fix the test code from week 9 quiz
# def test_my_number(my_number):
#     assert my_number == 13
