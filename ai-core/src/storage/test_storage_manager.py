from pathlib import Path

from .storage_manager import StorageManager


def main():

    manager = StorageManager()

    file = Path("storage/temp/manager_demo.txt")

    print()

    print("Save")
    print("----------------")

    manager.save(
        file,
        "Storage Manager Test",
    )

    print(manager.exists(file))

    print()

    print("Load")
    print("----------------")

    print(manager.load(file))

    print()

    print("Size")
    print("----------------")

    print(manager.size(file))

    print()

    print("Files")
    print("----------------")

    print(
        manager.list_files(
            Path("storage/temp")
        )
    )

    print()

    print("Delete")
    print("----------------")

    manager.delete(file)

    print(manager.exists(file))


if __name__ == "__main__":
    main()