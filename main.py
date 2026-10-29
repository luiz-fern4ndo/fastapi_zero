from http import HTTPStatus

from fastapi import FastAPI

from routes import auth, users
from schema import Message

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


@app.get('/', response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo!'}
