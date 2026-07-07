from .base_exception import FrameworkException


def main():

    try:

        raise FrameworkException(
            message="Framework initialization failed.",
            error_code="CORE001",
            status_code=500,
            module="AI Core",
            details={"component": "config"},
        )

    except FrameworkException as ex:

        print()

        print("Exception")
        print("--------------------")

        print(ex)

        print()

        print("Dictionary")
        print("--------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()