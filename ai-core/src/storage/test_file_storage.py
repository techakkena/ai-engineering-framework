from pathlib import Path

from .file_storage import FileStorage


def main():

    storage = FileStorage()

    file = Path("storage/temp/demo.txt")

    print()

    print("Save")
    print("--------------------")

    storage.save(
        file,
        "Hello AI Framework",
    )

    print(storage.exists(file))

    print()

    print("Load")

    print("--------------------")

    print(storage.load(file))

    print()

    print("Size")

    print("--------------------")

    print(storage.size(file))

    print()

    print("Files")

    print("--------------------")

    print(
        storage.list_files(
            Path("storage/temp"),
        )
    )

    print()

    print("Delete")

    print("--------------------")

    storage.delete(file)

    print(storage.exists(file))


if __name__ == "__main__":
    main()