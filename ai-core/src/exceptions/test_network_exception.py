from .network_exception import NetworkException


def main():

    try:

        raise NetworkException(
            message="Unable to connect to the OpenAI API.",
            details={
                "host": "api.openai.com",
                "reason": "Connection timeout",
            },
        )

    except NetworkException as ex:

        print()
        print("Network Exception")
        print("--------------------------")

        print(ex)

        print()

        print("Dictionary")
        print("--------------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()