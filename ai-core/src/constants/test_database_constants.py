from .database_constants import (
    DatabaseEngine,
    Transaction,
    SortOrder,
    DatabaseStatus,
)


def main():

    print()

    print("Database Engine")
    print("----------------")

    print(DatabaseEngine.SQLITE)

    print(DatabaseEngine.POSTGRESQL)

    print()

    print("Transaction")
    print("----------------")

    print(Transaction.COMMIT)

    print(Transaction.ROLLBACK)

    print()

    print("Sort")
    print("----------------")

    print(SortOrder.ASC)

    print()

    print("Status")
    print("----------------")

    print(DatabaseStatus.CONNECTED)


if __name__ == "__main__":
    main()