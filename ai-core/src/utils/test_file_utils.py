from pathlib import Path

from .file_utils import FileUtils


def main():

    file = Path("storage/temp/file_utils.txt")

    print()

    print("Write")
    print("----------------")

    FileUtils.write_text(
        file,
        "AI Framework",
    )

    print()

    print("Read")
    print("----------------")

    print(
        FileUtils.read_text(
            file,
        )
    )

    print()

    print("Size")
    print("----------------")

    print(
        FileUtils.size(
            file,
        )
    )

    print()

    copied = Path(
        "storage/temp/file_copy.txt"
    )

    FileUtils.copy(
        file,
        copied,
    )

    print("Copy")
    print("----------------")

    print(copied.exists())

    print()

    moved = Path(
        "storage/temp/file_move.txt"
    )

    FileUtils.move(
        copied,
        moved,
    )

    print("Move")
    print("----------------")

    print(moved.exists())

    print()

    renamed = FileUtils.rename(
        moved,
        "renamed.txt",
    )

    print("Rename")
    print("----------------")

    print(renamed.name)

    print()

    print("Delete")
    print("----------------")

    print(
        FileUtils.delete(
            renamed,
        )
    )

    print()

    FileUtils.delete(file)


if __name__ == "__main__":
    main()