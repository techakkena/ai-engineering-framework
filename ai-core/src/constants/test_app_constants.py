from .app_constants import (
    Application,
    Environment,
    HTTPStatus,
    ContentType,
    LogLevel,
)


def main():

    print()

    print("Application")

    print("----------------")

    print(Application.NAME)

    print(Application.VERSION)

    print(Application.DESCRIPTION)

    print()

    print("Environment")

    print("----------------")

    print(Environment.DEVELOPMENT)

    print()

    print("HTTP")

    print("----------------")

    print(HTTPStatus.OK)

    print(HTTPStatus.NOT_FOUND)

    print()

    print("Content Type")

    print("----------------")

    print(ContentType.JSON)

    print()

    print("Log Level")

    print("----------------")

    print(LogLevel.INFO.value)


if __name__ == "__main__":
    main()