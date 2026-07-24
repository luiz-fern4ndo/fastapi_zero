from http import HTTPStatus


def test_read_root_deve_retornar_ola_mundo(client):

    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post('/users/',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret'
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
            'username': 'bob',
            'email': 'bob@example.com',
            'id': 1
        }
