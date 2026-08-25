from http import HTTPStatus

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models import User
from schema import Message, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        raise HTTPException(
            detail='Username or Email already exist!',
            status_code=HTTPStatus.CONFLICT,
        )

    db_user = User(**user.model_dump())

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users/', response_model=UserList, status_code=HTTPStatus.OK)
def read_users(
    session: Session = Depends(get_session), limit: int = 10, offset: int = 0
):

    users = session.scalars(select(User).limit(limit).offset(offset))

    return {'users': users}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(
    user: UserSchema, user_id: int, session: Session = Depends(get_session)
):

    user_db = session.scalar(select(User).where(User.id == user_id))

    if not user_db:
        raise HTTPException(
            detail='User not found',
            status_code=HTTPStatus.NOT_FOUND
        )

    user_db.username = user.username
    user_db.email = user.email
    user_db.password = user.password

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db


@app.delete('/users/{user_id}',
            response_model=Message, status_code=HTTPStatus.OK)
def delete_user(user_id: int, session: Session = Depends(get_session)):

    user_db = session.scalar(select(User).where(User.id == user_id))

    if not user_db:
        raise HTTPException(
            detail='User not found',
            status_code=HTTPStatus.NOT_FOUND
        )

    session.delete(user_db)
    session.commit()

    return {'message': 'User deleted'}
