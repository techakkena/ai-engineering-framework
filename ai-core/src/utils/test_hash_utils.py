from pathlib import Path

from .hash_utils import HashUtils
from .file_utils import FileUtils


def main():

    print()

    print("MD5")
    print("----------------")

    print(HashUtils.md5("AI Framework"))

    print()

    print("SHA1")
    print("----------------")

    print(HashUtils.sha1("AI Framework"))

    print()

    print("SHA256")
    print("----------------")

    sha = HashUtils.sha256(
        "AI Framework"
    )

    print(sha)

    print()

    print("Verify")
    print("----------------")

    print(
        HashUtils.verify_sha256(
            "AI Framework",
            sha,
        )
    )

    print()

    file = Path(
        "storage/temp/hash_demo.txt"
    )

    FileUtils.write_text(
        file,
        "AI Framework",
    )

    print("File SHA256")
    print("----------------")

    print(
        HashUtils.file_sha256(
            file,
        )
    )

    FileUtils.delete(file)


if __name__ == "__main__":
    main()