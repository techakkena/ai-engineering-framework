from .auth_constants import (
    AuthProvider,
    AuthScheme,
    TokenType,
    JWT,
    UserRole,
    Permission,
)


def main():

    print()

    print("Authentication Providers")
    print("-----------------------------")

    print(AuthProvider.LOCAL)
    print(AuthProvider.GOOGLE)

    print()

    print("Authentication Scheme")
    print("-----------------------------")

    print(AuthScheme.BEARER)

    print()

    print("Token Types")
    print("-----------------------------")

    print(TokenType.ACCESS)
    print(TokenType.REFRESH)

    print()

    print("JWT")
    print("-----------------------------")

    print(JWT.ALGORITHM)
    print(JWT.ACCESS_TOKEN_EXPIRE_MINUTES)

    print()

    print("Roles")
    print("-----------------------------")

    print(UserRole.ADMIN)
    print(UserRole.USER)

    print()

    print("Permissions")
    print("-----------------------------")

    print(Permission.CREATE)
    print(Permission.DELETE)


if __name__ == "__main__":
    main()