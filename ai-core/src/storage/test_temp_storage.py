from .temp_storage import TempStorage


def main():

    temp = TempStorage()

    file = temp.create(
        ".txt",
        "Temporary File",
    )

    print()

    print("Created")

    print("----------------")

    print(file)

    print()

    print("Exists")

    print("----------------")

    print(temp.exists(file))

    print()

    print("Read")

    print("----------------")

    print(temp.read(file))

    print()

    print("Delete")

    print("----------------")

    temp.delete(file)

    print(temp.exists(file))


if __name__ == "__main__":
    main()