"""
These tests are not meant to be runnable - they're here for syntax highlighting/etc.

All classes/setup code are stubs.
"""

from dataclasses import dataclass

class UserService:
    def create_user(self, username):
        return username


class App:
    def post(self, path):
        def f():
            return path

        return f


user_service = UserService()
app = App()


@dataclass
class User:
    username: str
    password: int

    id: int = None


@app.post("/users")
def create_user(username: str):
    return user_service.create_user(username=username)


def test_can_create_user(client, db_session):
    response = client.post("/users", json={
        "username": "foobar",
    })

    assert response.status_code == 201
    created_user = response.data

    db_user = db_session.query(User) \
        .filter(User.id == created_user['id']) \
        .first()

    assert db_user["username"] == "foobar"
    assert db_user["id"]


def test_can_fetch_user(client, created_user):
    response = client.get(f"/users/{created_user['id']}")

    assert response.status_code == 200

    fetched_user = response.data
    assert created_user == fetched_user



