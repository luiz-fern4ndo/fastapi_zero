from http import HTTPStatus


def test_read_root_deve_retornar_ola_mundo(client):

    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'alice', 'email': 'alice@example.com', 'id': 1}]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NO_CONTENT


def test_update_user_should_return_not_found__exercicio(client):
    resposne = client.put(
        '/users/10',
        json={
            'username': 'alice',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert resposne.status_code == HTTPStatus.NOT_FOUND
    assert resposne.json() == {'detail': 'User not found!'}


def test_delete_user_should_return_not_found__exercicio(client):
    resposne = client.delete('/users/10')

    assert resposne.status_code == HTTPStatus.NOT_FOUND
    assert resposne.json() == {'detail': 'User not found!'}
