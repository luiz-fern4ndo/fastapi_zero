from dataclasses import asdict

from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User


def test_create_user(session: Session, mock_db_time):

    with mock_db_time(model=User) as time:
        new_user = User(
            username='bob', email='bob@example.com', password='secret'
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        user = session.scalar(select(User).where(User.id == 1))

        assert asdict(user) == {
            'id': 1,
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
            'created_at': time,
            'updated_at': time,
        }
