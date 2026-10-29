from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import get_session
from models import User
from schema import Message, UserList, UserPublic, UserSchema
from security import get_current_user, get_password_hash

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):

    db_user = session.scalar(
        select(User).where(
            (User.email == user.email) | (User.email == user.email)
        )
    )

    if db_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='USername or Email already exists',
        )

    db_user = User(**user.model_dump())
    db_user.password = get_password_hash(user.password)

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get('/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users(
    current_user=Depends(get_current_user),
    session: Session = Depends(get_session),
    limit=10,
    offset=0,
):

    users = session.scalars(select(User).limit(limit).offset(offset))

    return {'users': users}


@router.get('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def read_user__exercicio(
    user_id: int,
    session: Session = Depends(get_session),
):

    user = session.scalar(select(User).where(User.id == user_id))

    if not user:
        raise HTTPException(
            detail='User not found', status_code=HTTPStatus.NOT_FOUND
        )

    return user


@router.put('/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic)
def update_user(
    user: UserSchema,
    user_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )
    try:
        current_user.username = user.username
        current_user.email = user.email
        current_user.password = get_password_hash(user.password)
        session.commit()
        session.refresh(current_user)

        return current_user

    except IntegrityError:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail='Username or Email already exists',
        )


@router.delete('/{user_id}', status_code=HTTPStatus.OK, response_model=Message)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if user_id != current_user.id:
        raise HTTPException(
            status_code=HTTPStatus.FORBIDDEN, detail='Not enough permissions'
        )

    session.delete(current_user)
    session.commit()

    return {'message': 'User deleted'}
