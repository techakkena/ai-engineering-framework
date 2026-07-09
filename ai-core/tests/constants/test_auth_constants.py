from constants.auth_constants import (
    AuthProvider,
    AuthScheme,
    TokenType,
    JWT,
    UserRole,
    Permission,
)


def test_auth_provider():
    assert AuthProvider.LOCAL == "local"
    assert AuthProvider.GOOGLE == "google"
    assert AuthProvider.MICROSOFT == "microsoft"
    assert AuthProvider.GITHUB == "github"
    assert AuthProvider.FACEBOOK == "facebook"
    assert AuthProvider.LINKEDIN == "linkedin"


def test_auth_scheme():
    assert AuthScheme.BEARER == "Bearer"
    assert AuthScheme.BASIC == "Basic"
    assert AuthScheme.API_KEY == "ApiKey"


def test_token_type():
    assert TokenType.ACCESS == "access"
    assert TokenType.REFRESH == "refresh"


def test_jwt():
    assert JWT.ALGORITHM == "HS256"
    assert JWT.ACCESS_TOKEN_EXPIRE_MINUTES == 30
    assert JWT.REFRESH_TOKEN_EXPIRE_DAYS == 7


def test_user_role():
    assert UserRole.SUPER_ADMIN == "super_admin"
    assert UserRole.ADMIN == "admin"
    assert UserRole.MANAGER == "manager"
    assert UserRole.USER == "user"
    assert UserRole.GUEST == "guest"


def test_permission():
    assert Permission.CREATE == "create"
    assert Permission.READ == "read"
    assert Permission.UPDATE == "update"
    assert Permission.DELETE == "delete"
    assert Permission.EXECUTE == "execute"

