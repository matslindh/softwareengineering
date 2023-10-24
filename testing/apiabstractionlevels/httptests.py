"""
These tests are not meant to be runnable - they're here for syntax highlighting/etc.

All classes/setup code are stubs.
"""


class UserService:
    def create_user(self, username):
        return username

    def get_user(self, user_id):
        return None


class App:
    def post(self, path):
        def f():
            return path

        return f

    def get(self, path):
        def f():
            return path

        return f


user_service = UserService()
app = App()


@app.post("/users")
def create_user(username: str):
    return user_service.create_user(username=username)


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_service.get_user(user_id=user_id)


def test_can_create_user(client):
    response = client.post("/users", json={
        "username": "foobar",
    })

    assert response.status_code == 201

    user = response.data
    assert user["username"] == "foobar"
    assert user["id"]


def test_can_fetch_user(client, created_user):
    response = client.get(f"/users/{created_user['id']}")

    assert response.status_code == 200

    fetched_user = response.data
    assert created_user == fetched_user



