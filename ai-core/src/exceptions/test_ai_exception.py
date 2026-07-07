from .ai_exception import AIException


def main():

    try:

        raise AIException(
            message="Embedding generation failed.",
            details={
                "model": "text-embedding-3-small",
                "reason": "Token limit exceeded",
            },
        )

    except AIException as ex:

        print()
        print("AI Exception")
        print("-----------------------")
        print(ex)

        print()
        print("Dictionary")
        print("-----------------------")
        print(ex.to_dict())


if __name__ == "__main__":
    main()