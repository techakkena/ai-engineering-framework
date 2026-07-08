from .storage_factory import StorageFactory
from constants.storage_constants import StorageTypes


def main():

    storage = StorageFactory.create(
        StorageTypes.LOCAL
    )

    print()

    print("Storage Provider")
    print("--------------------")

    print(type(storage).__name__)


if __name__ == "__main__":
    main()