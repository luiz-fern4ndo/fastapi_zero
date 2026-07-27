from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from schema import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', status_code=HTTPStatus.OK,
         response_model=UserPublic)
def update_user(user: UserSchema, user_id: int):

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            detail='User not found!',
            status_code=HTTPStatus.NOT_FOUND
        )

    user = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user

    return user


@app.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
def delete_user(user_id: int):

    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            detail='User not found!',
            status_code=HTTPStatus.NOT_FOUND
        )
    del (database[user_id - 1])
