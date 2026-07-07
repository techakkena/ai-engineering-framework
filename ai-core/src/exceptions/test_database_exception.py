from .database_exception import DatabaseException


def main():

    try:

        raise DatabaseException(
            message="Unable to connect to the database.",
            details={
                "database": "framework.db",
                "reason": "Connection timeout",
            },
        )

    except DatabaseException as ex:

        print()
        print("Database Exception")
        print("--------------------------")

        print(ex)

        print()

        print("Dictionary")
        print("--------------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()