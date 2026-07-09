from base.base_model import BaseModel


class User(BaseModel):

    def __init__(self):
        super().__init__()

        self.name = "John"
        self.email = "john@example.com"


def test_user_creation():
    user = User()

    assert user is not None
    assert user.name == "John"
    assert user.email == "john@example.com"
    assert user.is_active is True


def test_to_dict():
    user = User()

    data = user.to_dict()

    assert isinstance(data, dict)
    assert data["name"] == "John"
    assert data["email"] == "john@example.com"


def test_update():
    user = User()

    user.update(
        name="Alice",
        email="alice@example.com",
    )

    assert user.name == "Alice"
    assert user.email == "alice@example.com"


def test_deactivate():
    user = User()

    user.deactivate()

    assert user.is_active is False


def test_activate():
    user = User()

    user.deactivate()
    user.activate()

    assert user.is_active is True