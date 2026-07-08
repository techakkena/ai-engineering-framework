from .id_utils import (
    generate_uuid,
    generate_token,
    generate_short_id,
)


def main():

    print()

    print("UUID")
    print("----------------")

    print(generate_uuid())

    print()

    print("Token")
    print("----------------")

    print(generate_token())

    print()

    print("Short ID")
    print("----------------")

    print(generate_short_id())


if __name__ == "__main__":
    main()