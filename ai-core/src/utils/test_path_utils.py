from pathlib import Path

from .path_utils import PathUtils


def main():

    file = Path("storage/temp/demo.txt")

    print()

    print("Ensure Directory")
    print("----------------")

    PathUtils.ensure_directory(file)

    print(PathUtils.exists(file.parent))

    print()

    print("File Name")
    print("----------------")

    print(PathUtils.file_name(file))

    print()

    print("Extension")
    print("----------------")

    print(PathUtils.extension(file))

    print()

    print("Parent")
    print("----------------")

    print(PathUtils.parent(file))

    print()

    print("Join")
    print("----------------")

    print(
        PathUtils.join(
            "storage",
            "uploads",
            "test.txt",
        )
    )

    print()

    print("Resolve")
    print("----------------")

    print(PathUtils.resolve(file))


if __name__ == "__main__":
    main()