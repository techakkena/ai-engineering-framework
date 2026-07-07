from .not_found_exception import NotFoundException


def main():

    try:

        raise NotFoundException(
            message="User record not found.",
            details={
                "resource": "User",
                "id": 101,
            },
        )

    except NotFoundException as ex:

        print()
        print("Not Found Exception")
        print("---------------------------")
        print(ex)

        print()
        print("Dictionary")
        print("---------------------------")
        print(ex.to_dict())


if __name__ == "__main__":
    main()