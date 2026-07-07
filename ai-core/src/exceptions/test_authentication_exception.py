from .authentication_exception import AuthenticationException


def main():

    try:

        raise AuthenticationException(
            message="Invalid username or password.",
            details={
                "username": "admin",
                "reason": "Invalid credentials",
            },
        )

    except AuthenticationException as ex:

        print()
        print("Authentication Exception")
        print("-----------------------------")

        print(ex)

        print()

        print("Dictionary")
        print("-----------------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()