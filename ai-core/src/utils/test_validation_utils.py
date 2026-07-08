from .validation_utils import ValidationUtils


def main():

    print()

    print("Email")
    print("----------------")

    print(
        ValidationUtils.is_email(
            "admin@example.com"
        )
    )

    print()

    print("URL")
    print("----------------")

    print(
        ValidationUtils.is_url(
            "https://openai.com"
        )
    )

    print()

    print("UUID")
    print("----------------")

    print(
        ValidationUtils.is_uuid(
            "550e8400-e29b-41d4-a716-446655440000"
        )
    )

    print()

    print("JSON")
    print("----------------")

    print(
        ValidationUtils.is_json(
            '{"name":"AI"}'
        )
    )

    print()

    print("Number")
    print("----------------")

    print(
        ValidationUtils.is_number(
            "123.45"
        )
    )

    print()

    print("IP")
    print("----------------")

    print(
        ValidationUtils.is_ip_address(
            "192.168.1.1"
        )
    )

    print()

    print("Filename")
    print("----------------")

    print(
        ValidationUtils.is_filename(
            "resume.pdf"
        )
    )

    print()

    print("Extension")
    print("----------------")

    print(
        ValidationUtils.has_extension(
            "resume.pdf",
            ".pdf",
            ".docx",
        )
    )


if __name__ == "__main__":
    main()