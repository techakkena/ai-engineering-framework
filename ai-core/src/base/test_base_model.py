from .base_model import BaseModel


class User(BaseModel):

    def __init__(self):

        super().__init__()

        self.name = "John"

        self.email = "john@example.com"


def main():

    user = User()

    print()

    print("Initial")

    print("--------------------")

    print(user.to_dict())

    print()

    print(user.name)

    print(user.email)

    print()

    user.update(
        name="Alice",
        email="alice@example.com",
    )

    print("Updated")

    print("--------------------")

    print(user.name)

    print(user.email)

    print()

    user.deactivate()

    print(user.is_active)

    print()

    user.activate()

    print(user.is_active)


if __name__ == "__main__":
    main()