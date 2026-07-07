from .integration_exception import IntegrationException


def main():

    try:

        raise IntegrationException(
            message="Google Drive API request failed.",
            details={
                "service": "Google Drive",
                "reason": "Invalid access token",
            },
        )

    except IntegrationException as ex:

        print()
        print("Integration Exception")
        print("------------------------------")
        print(ex)

        print()
        print("Dictionary")
        print("------------------------------")
        print(ex.to_dict())


if __name__ == "__main__":
    main()