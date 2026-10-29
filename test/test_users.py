from http import HTTPStatus

from schema import UserPublic


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


# def test_read_users_with_users(client, user):
#     response = client.get('/users/')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'users': [
#             {
#                 'username': 'alice',
#                 'email': 'alice@example.com',
#                 'id': 1,
#             }
#         ]
#     }


def test_read_users(client, user, token):
    user_schema = UserPublic.model_validate(user).model_dump()

    response = client.get(
        '/users/', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
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


def test_get_user___exercicio(client, user):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test',
        'email': 'test@test.com',
        'id': 1,
    }


def test_delete_user(client, user, token):
    response = client.delete(
        '/users/1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_update_user_should_return_not_found__exercicio(client, user, token):
    response = client.put(
        '/users/999',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}


def test_delete_user_should_return_not_found__exercicio(client, token):
    response = client.delete(
        '/users/999',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert response.json() == {'detail': 'Not enough permissions'}
