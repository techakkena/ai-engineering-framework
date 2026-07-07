from .configuration_exception import ConfigurationException

def main():

    try:

        raise ConfigurationException(
            message="SECRET_KEY environment variable is missing.",
            details={
                "variable": "SECRET_KEY",
                "source": ".env",
            },
        )

    except ConfigurationException as ex:

        print()
        print("Configuration Exception")
        print("------------------------------")

        print(ex)

        print()

        print("Dictionary")
        print("------------------------------")

        print(ex.to_dict())


if __name__ == "__main__":
    main()