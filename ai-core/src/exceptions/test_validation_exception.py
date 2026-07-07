from .validation_exception import ValidationException


def main():

    try:

        raise ValidationException(
            message="Email address is required.",
            details={
                "field": "email",
                "value": None,
            },
        )

    except ValidationException as ex:

        print()
        print("Validation Exception")
        print("---------------------------")

        print(ex)

        print()

        print("Dictionary")
        print("---------------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()