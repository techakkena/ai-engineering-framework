from .error_constants import ErrorMessage, ErrorCategory


def main():

    print()

    print("Error Messages")
    print("--------------------------")

    print(ErrorMessage.UNKNOWN)
    print(ErrorMessage.INVALID_REQUEST)
    print(ErrorMessage.ACCESS_DENIED)

    print()

    print("Categories")
    print("--------------------------")

    print(ErrorCategory.VALIDATION)
    print(ErrorCategory.AUTHENTICATION)
    print(ErrorCategory.DATABASE)
    print(ErrorCategory.AI)


if __name__ == "__main__":
    main()