"""
AI Engineering Framework
Authentication Constants

Author : TECHAKKENA
"""


class AuthProvider:
    """
    Supported authentication providers.
    """

    LOCAL = "local"
    GOOGLE = "google"
    MICROSOFT = "microsoft"
    GITHUB = "github"
    FACEBOOK = "facebook"
    LINKEDIN = "linkedin"


class AuthScheme:
    """
    Authentication schemes.
    """

    BEARER = "Bearer"
    BASIC = "Basic"
    API_KEY = "ApiKey"


class TokenType:
    """
    Token types.
    """

    ACCESS = "access"
    REFRESH = "refresh"


class JWT:
    """
    JWT defaults.
    """

    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    REFRESH_TOKEN_EXPIRE_DAYS = 7


class UserRole:
    """
    Default framework roles.
    """

    SUPER_ADMIN = "super_admin"

    ADMIN = "admin"

    MANAGER = "manager"

    USER = "user"

    GUEST = "guest"


class Permission:
    """
    Common permissions.
    """

    CREATE = "create"

    READ = "read"

    UPDATE = "update"

    DELETE = "delete"

    EXECUTE = "execute"
