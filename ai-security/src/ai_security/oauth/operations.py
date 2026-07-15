"""
Framework-independent OAuth operations.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from ai_security.oauth.constants import (
    DEFAULT_GRANT_TYPE,
    DEFAULT_TOKEN_TYPE,
    SUPPORTED_GRANT_TYPES,
)
from ai_security.oauth.exceptions import (
    OAuthConfigurationError,
    OAuthTokenError,
)


@dataclass(slots=True, frozen=True)
class OAuthClient:
    """OAuth client configuration."""

    client_id: str
    client_secret: str
    grant_type: str = DEFAULT_GRANT_TYPE


@dataclass(slots=True, frozen=True)
class OAuthToken:
    """OAuth access token."""

    access_token: str
    token_type: str = DEFAULT_TOKEN_TYPE
    expires_at: datetime | None = None
    refresh_token: str | None = None


class OAuthService:
    """Framework-independent OAuth service."""

    def validate_client(self, client: OAuthClient) -> bool:
        """Validate an OAuth client."""
        if client.grant_type not in SUPPORTED_GRANT_TYPES:
            raise OAuthConfigurationError(
                f"Unsupported grant type: {client.grant_type}"
            )

        if not client.client_id:
            raise OAuthConfigurationError(
                "Client ID cannot be empty."
            )

        if not client.client_secret:
            raise OAuthConfigurationError(
                "Client secret cannot be empty."
            )

        return True

    def issue_token(
        self,
        client: OAuthClient,
        *,
        lifetime_seconds: int = 3600,
    ) -> OAuthToken:
        """
        Issue an OAuth token.

        This is a placeholder implementation intended to define the
        framework API. Concrete integrations should override this
        method to communicate with an OAuth provider.
        """
        self.validate_client(client)

        expires_at = datetime.now(UTC) + timedelta(
            seconds=lifetime_seconds
        )

        return OAuthToken(
            access_token="ACCESS_TOKEN_PLACEHOLDER",
            expires_at=expires_at,
            refresh_token="REFRESH_TOKEN_PLACEHOLDER",
        )

    def refresh_token(
        self,
        refresh_token: str,
    ) -> OAuthToken:
        """
        Refresh an OAuth token.

        Concrete providers should override this implementation.
        """
        raise OAuthTokenError(
            "OAuth token refresh requires a concrete provider."
        )

    def revoke_token(
        self,
        access_token: str,
    ) -> bool:
        """
        Revoke an OAuth token.

        Concrete providers should override this implementation.
        """
        raise OAuthTokenError(
            "OAuth token revocation requires a concrete provider."
        )