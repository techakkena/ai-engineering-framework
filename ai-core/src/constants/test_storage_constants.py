from .storage_constants import (
    StorageDirectory,
    FileExtension,
    FileSize,
    storage_types,
)


def main():

    print()

    print("Storage Directories")
    print("---------------------------")

    print(StorageDirectory.UPLOADS)
    print(StorageDirectory.LOGS)
    print(StorageDirectory.VECTOR_DB)

    print()

    print("Extensions")
    print("---------------------------")

    print(FileExtension.PDF)
    print(FileExtension.JSON)

    print()

    print("File Sizes")
    print("---------------------------")

    print("1 KB =", FileSize.KB)
    print("1 MB =", FileSize.MB)
    print("1 GB =", FileSize.GB)


if __name__ == "__main__":
    main()