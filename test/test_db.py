from dataclasses import asdict

from sqlalchemy import select

from models import User


def test_create_app(session, mock_db_time):

    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', email='alice@email.com', password='secret'
        )

        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        user = session.scalar(select(User).where(User.username == 'alice'))

        assert asdict(user) == {
            'id': 1,
            'username': 'alice',
            'email': 'alice@email.com',
            'password': 'secret',
            'created_at': time,
            'updated_at': time
        }
