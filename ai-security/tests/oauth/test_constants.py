"""
Tests for ai_security.oauth.constants.
"""

from ai_security.oauth.constants import (
    DEFAULT_GRANT_TYPE,
    DEFAULT_RESPONSE_TYPE,
    DEFAULT_TOKEN_TYPE,
    SUPPORTED_GRANT_TYPES,
)


def test_default_grant_type() -> None:
    """Test default grant type."""
    assert DEFAULT_GRANT_TYPE == "client_credentials"


def test_default_response_type() -> None:
    """Test default response type."""
    assert DEFAULT_RESPONSE_TYPE == "code"


def test_default_token_type() -> None:
    """Test default token type."""
    assert DEFAULT_TOKEN_TYPE == "Bearer"


def test_supported_grant_types() -> None:
    """Test supported grant types."""
    assert "authorization_code" in SUPPORTED_GRANT_TYPES
    assert "client_credentials" in SUPPORTED_GRANT_TYPES
    assert "password" in SUPPORTED_GRANT_TYPES
    assert "refresh_token" in SUPPORTED_GRANT_TYPES
    assert "device_code" in SUPPORTED_GRANT_TYPES
    assert len(SUPPORTED_GRANT_TYPES) == 5