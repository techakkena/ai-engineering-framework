from pathlib import Path

from .storage_provider import StorageProvider


class DemoStorage(StorageProvider):

    def save(self, file_path: Path, data):
        print(f"Saving {file_path}")
        return True

    def load(self, file_path: Path):
        return "Loaded Data"

    def delete(self, file_path: Path):
        print(f"Deleting {file_path}")
        return True

    def exists(self, file_path: Path):
        return True

    def list_files(self, directory: Path):
        return ["sample.txt", "demo.pdf"]

    def size(self, file_path: Path):
        return 2048


def main():

    storage = DemoStorage()

    file_path = Path("storage/uploads/demo.txt")

    print()

    print("Save")
    print("----------------")
    print(storage.save(file_path, "Hello"))

    print()

    print("Load")
    print("----------------")
    print(storage.load(file_path))

    print()

    print("Exists")
    print("----------------")
    print(storage.exists(file_path))

    print()

    print("Files")
    print("----------------")
    print(storage.list_files(Path("storage/uploads")))

    print()

    print("Size")
    print("----------------")
    print(storage.size(file_path))

    print()

    print("Delete")
    print("----------------")
    print(storage.delete(file_path))


if __name__ == "__main__":
    main()