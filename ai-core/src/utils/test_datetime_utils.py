from .datetime_utils import DateTimeUtils


def main():

    print()

    print("Now")
    print("----------------")

    print(DateTimeUtils.now())

    print()

    print("UTC")
    print("----------------")

    print(DateTimeUtils.utc_now())

    print()

    print("Today")
    print("----------------")

    print(DateTimeUtils.today())

    print()

    print("Timestamp")
    print("----------------")

    print(DateTimeUtils.timestamp())

    print()

    print("ISO")
    print("----------------")

    print(DateTimeUtils.iso_now())

    print()

    print("Format")
    print("----------------")

    print(
        DateTimeUtils.format(
            DateTimeUtils.now()
        )
    )

    print()

    print("Parse")
    print("----------------")

    print(
        DateTimeUtils.parse(
            "2026-07-08 10:30:00"
        )
    )


if __name__ == "__main__":
    main()