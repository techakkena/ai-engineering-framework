"""
Unit tests for ai_api.authentication.constants.
"""

from __future__ import annotations

from ai_api.authentication.constants import (
    API_KEY_HEADER,
    API_KEY_PREFIX,
    AUDIENCE_CLAIM,
    AUTHORIZATION_HEADER,
    BASIC_PREFIX,
    BEARER_PREFIX,
    DEFAULT_CLOCK_SKEW,
    DEFAULT_REFRESH_TOKEN_EXPIRATION,
    DEFAULT_TOKEN_EXPIRATION,
    DIGEST_PREFIX,
    EXPIRES_AT_CLAIM,
    ISSUED_AT_CLAIM,
    ISSUER_CLAIM,
    JWT_ID_CLAIM,
    MAX_API_KEY_LENGTH,
    MAX_PASSWORD_LENGTH,
    MAX_USERNAME_LENGTH,
    MIN_API_KEY_LENGTH,
    MIN_PASSWORD_LENGTH,
    MIN_USERNAME_LENGTH,
    NOT_BEFORE_CLAIM,
    SUBJECT_CLAIM,
    SUPPORTED_AUTH_SCHEMES,
    TOKEN_HEADER,
    TOKEN_TYPE,
)


def test_authorization_headers() -> None:
    """Test authentication headers."""
    assert AUTHORIZATION_HEADER == "Authorization"
    assert API_KEY_HEADER == "X-API-Key"
    assert TOKEN_HEADER == "X-Access-Token"


def test_authentication_prefixes() -> None:
    """Test authentication prefixes."""
    assert BEARER_PREFIX == "Bearer"
    assert BASIC_PREFIX == "Basic"
    assert DIGEST_PREFIX == "Digest"
    assert TOKEN_TYPE == "Bearer"


def test_supported_auth_schemes() -> None:
    """Test supported authentication schemes."""
    expected = {
        "bearer",
        "basic",
        "apikey",
        "oauth2",
        "jwt",
        "session",
    }

    assert SUPPORTED_AUTH_SCHEMES == expected


def test_supported_auth_schemes_are_immutable() -> None:
    """Supported authentication schemes should be immutable."""
    assert isinstance(
        SUPPORTED_AUTH_SCHEMES,
        frozenset,
    )


def test_token_expiration_defaults() -> None:
    """Test token expiration defaults."""
    assert DEFAULT_TOKEN_EXPIRATION == 3600
    assert DEFAULT_REFRESH_TOKEN_EXPIRATION == 86400
    assert DEFAULT_CLOCK_SKEW == 60


def test_jwt_claim_names() -> None:
    """Test JWT claim constants."""
    assert SUBJECT_CLAIM == "sub"
    assert ISSUER_CLAIM == "iss"
    assert AUDIENCE_CLAIM == "aud"
    assert ISSUED_AT_CLAIM == "iat"
    assert EXPIRES_AT_CLAIM == "exp"
    assert NOT_BEFORE_CLAIM == "nbf"
    assert JWT_ID_CLAIM == "jti"


def test_api_key_configuration() -> None:
    """Test API key defaults."""
    assert API_KEY_PREFIX == "ak"
    assert MIN_API_KEY_LENGTH == 32
    assert MAX_API_KEY_LENGTH == 256


def test_password_policy() -> None:
    """Test password policy."""
    assert MIN_PASSWORD_LENGTH == 8
    assert MAX_PASSWORD_LENGTH == 128


def test_username_policy() -> None:
    """Test username policy."""
    assert MIN_USERNAME_LENGTH == 3
    assert MAX_USERNAME_LENGTH == 64