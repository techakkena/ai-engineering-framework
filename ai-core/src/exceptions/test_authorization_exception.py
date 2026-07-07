from .authorization_exception import AuthorizationException


def main():

    try:

        raise AuthorizationException(
            message="Access denied. Administrator role required.",
            details={
                "required_role": "Administrator",
                "current_role": "User",
            },
        )

    except AuthorizationException as ex:

        print()
        print("Authorization Exception")
        print("------------------------------")

        print(ex)

        print()

        print("Dictionary")
        print("------------------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()