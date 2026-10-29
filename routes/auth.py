from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models import User
from schema import Token
from security import create_access_token, verify_password

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/', status_code=HTTPStatus.OK, response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):

    user = session.scalar(select(User).where(User.email == form_data.username))

    credencials_exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Incorrect email or password',
    )

    if not user:
        raise credencials_exception

    if not verify_password(form_data.password, user.password):
        raise credencials_exception

    access_token = create_access_token({'sub': user.email})

    return {'access_token': access_token, 'token_type': 'Bearer'}
