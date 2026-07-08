from pathlib import Path

from .json_utils import JsonUtils


def main():

    data = {
        "framework": "AI Engineering Framework",
        "version": "0.1.0",
        "modules": [
            "storage",
            "base",
            "utils",
        ],
    }

    file = Path("storage/temp/framework.json")

    print()

    print("Write")
    print("----------------")

    JsonUtils.write(
        file,
        data,
    )

    print(file.exists())

    print()

    print("Read")
    print("----------------")

    print(
        JsonUtils.read(
            file,
        )
    )

    print()

    print("JSON String")
    print("----------------")

    print(
        JsonUtils.dumps(data)
    )

    print()

    print("Pretty Print")
    print("----------------")

    JsonUtils.pretty_print(data)


if __name__ == "__main__":
    main()