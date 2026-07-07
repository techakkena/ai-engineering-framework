from .file_exception import FileException


def main():

    try:

        raise FileException(
            message="Unsupported file format.",
            details={
                "filename": "resume.exe",
                "allowed_formats": [
                    "pdf",
                    "docx",
                    "txt",
                ],
            },
        )

    except FileException as ex:

        print()
        print("File Exception")
        print("-----------------------")

        print(ex)

        print()

        print("Dictionary")
        print("-----------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()