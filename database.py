from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import table_registry


def get_session():
    engine = create_engine('sqlite:///database.db')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session
