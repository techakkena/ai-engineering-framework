from .api_constants import (
    API,
    HTTPMethod,
    Header,
    MimeType,
    ResponseMessage,
)


def main():

    print()
    print("API")
    print("----------------")
    print(API.API_PREFIX)
    print(API.DEFAULT_PORT)

    print()
    print("HTTP Method")
    print("----------------")
    print(HTTPMethod.GET)
    print(HTTPMethod.POST)

    print()
    print("Headers")
    print("----------------")
    print(Header.AUTHORIZATION)

    print()
    print("Mime Types")
    print("----------------")
    print(MimeType.JSON)

    print()
    print("Messages")
    print("----------------")
    print(ResponseMessage.SUCCESS)


if __name__ == "__main__":
    main()