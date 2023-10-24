"""
These tests are not meant to be runnable - they're here for syntax highlighting/etc.

All classes/setup code are stubs.
"""

from dataclasses import dataclass
from pytest import fixture


class Session:
    pass


@dataclass
class User:
    username: str
    password: int

    id: int = None


class UserService:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_user(self, username: str, password: int):
        user = User(username=username, password=password)

        self.db_session.add(user)
        self.db_session.commit()

        return user

    def get_user_from_user_id(self, user_id: int) -> User:
        return self.db_session.query(User) \
            .filter(User.id == user_id) \
            .first()


@fixture
def user_service(db_session):
    return UserService(db_session=db_session)


@fixture
def db_session():
    return Session()


def test_can_create_user(user_service):
    user = user_service.create_user(username="test", password=123)

    assert user.id
    assert user.username == "test"


def test_can_get_user(user_service):
    user = user_service.create_user(username="test", password=123)
    fetched_user = user_service.get_user_from_user_id(user_id=user.id)

    assert fetched_user == user

