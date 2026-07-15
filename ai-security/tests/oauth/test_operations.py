"""
Tests for ai_security.oauth.operations.
"""

from datetime import UTC, datetime

import pytest

from ai_security.oauth.exceptions import (
    OAuthConfigurationError,
    OAuthTokenError,
)
from ai_security.oauth.operations import (
    OAuthClient,
    OAuthService,
    OAuthToken,
)


def test_validate_client_success() -> None:
    """Test validating a valid OAuth client."""
    service = OAuthService()

    client = OAuthClient(
        client_id="client-id",
        client_secret="client-secret",
    )

    assert service.validate_client(client) is True


def test_validate_client_invalid_grant_type() -> None:
    """Test invalid grant type."""
    service = OAuthService()

    client = OAuthClient(
        client_id="client",
        client_secret="secret",
        grant_type="invalid",
    )

    with pytest.raises(OAuthConfigurationError):
        service.validate_client(client)


def test_validate_client_missing_client_id() -> None:
    """Test missing client id."""
    service = OAuthService()

    client = OAuthClient(
        client_id="",
        client_secret="secret",
    )

    with pytest.raises(OAuthConfigurationError):
        service.validate_client(client)


def test_validate_client_missing_client_secret() -> None:
    """Test missing client secret."""
    service = OAuthService()

    client = OAuthClient(
        client_id="client",
        client_secret="",
    )

    with pytest.raises(OAuthConfigurationError):
        service.validate_client(client)


def test_issue_token() -> None:
    """Test issuing a token."""
    service = OAuthService()

    client = OAuthClient(
        client_id="client",
        client_secret="secret",
    )

    token = service.issue_token(client)

    assert isinstance(token, OAuthToken)
    assert token.access_token == "ACCESS_TOKEN_PLACEHOLDER"
    assert token.refresh_token == "REFRESH_TOKEN_PLACEHOLDER"
    assert token.token_type == "Bearer"
    assert token.expires_at is not None
    assert token.expires_at > datetime.now(UTC)


def test_issue_token_custom_lifetime() -> None:
    """Test issuing a token with custom lifetime."""
    service = OAuthService()

    client = OAuthClient(
        client_id="client",
        client_secret="secret",
    )

    token = service.issue_token(
        client,
        lifetime_seconds=600,
    )

    assert token.expires_at is not None

    remaining = (
        token.expires_at - datetime.now(UTC)
    ).total_seconds()

    assert remaining <= 600
    assert remaining > 590


def test_refresh_token_not_implemented() -> None:
    """Test refresh token placeholder."""
    service = OAuthService()

    with pytest.raises(OAuthTokenError):
        service.refresh_token("refresh-token")


def test_revoke_token_not_implemented() -> None:
    """Test revoke token placeholder."""
    service = OAuthService()

    with pytest.raises(OAuthTokenError):
        service.revoke_token("access-token")


def test_oauth_client_defaults() -> None:
    """Test OAuthClient defaults."""
    client = OAuthClient(
        client_id="client",
        client_secret="secret",
    )

    assert client.grant_type == "client_credentials"


def test_oauth_token_defaults() -> None:
    """Test OAuthToken defaults."""
    token = OAuthToken(access_token="abc123")

    assert token.access_token == "abc123"
    assert token.token_type == "Bearer"
    assert token.refresh_token is None
    assert token.expires_at is None