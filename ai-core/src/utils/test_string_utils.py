from .string_utils import StringUtils


def main():

    print()

    print("Empty")
    print("----------------")

    print(StringUtils.is_empty(""))

    print()

    print("Truncate")
    print("----------------")

    print(
        StringUtils.truncate(
            "Artificial Intelligence Framework",
            20,
        )
    )

    print()

    print("Remove Spaces")
    print("----------------")

    print(
        StringUtils.remove_extra_spaces(
            "AI     Engineering     Framework"
        )
    )

    print()

    print("Title Case")
    print("----------------")

    print(
        StringUtils.title_case(
            "artificial intelligence"
        )
    )

    print()

    print("Snake Case")
    print("----------------")

    print(
        StringUtils.snake_case(
            "AIFrameworkCore"
        )
    )

    print()

    print("Camel Case")
    print("----------------")

    print(
        StringUtils.camel_case(
            "ai_framework_core"
        )
    )

    print()

    print("Slug")
    print("----------------")

    print(
        StringUtils.slugify(
            "AI Engineering Framework!"
        )
    )


if __name__ == "__main__":
    main()