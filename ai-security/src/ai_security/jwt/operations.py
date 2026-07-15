"""
Framework-independent JWT operations.

This module intentionally provides a lightweight abstraction that does
not depend on any third-party JWT library. Concrete implementations can
extend this service or adapt it to libraries such as PyJWT, Authlib,
python-jose, etc.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any

from ai_security.jwt.constants import (
    DEFAULT_ALGORITHM,
    DEFAULT_AUDIENCE,
    DEFAULT_EXPIRATION_SECONDS,
    DEFAULT_ISSUER,
    SUPPORTED_ALGORITHMS,
)
from ai_security.jwt.exceptions import (
    JWTConfigurationError,
    JWTDecodeError,
)


@dataclass(slots=True, frozen=True)
class JWTClaims:
    """Represents standard JWT claims."""

    subject: str
    issuer: str = DEFAULT_ISSUER
    audience: str = DEFAULT_AUDIENCE
    expires_at: datetime | None = None
    additional_claims: dict[str, Any] = field(default_factory=dict)


class JWTService:
    """Framework-independent JWT service."""

    def __init__(
        self,
        *,
        algorithm: str = DEFAULT_ALGORITHM,
        expiration_seconds: int = DEFAULT_EXPIRATION_SECONDS,
    ) -> None:
        if algorithm not in SUPPORTED_ALGORITHMS:
            raise JWTConfigurationError(
                f"Unsupported JWT algorithm: {algorithm}"
            )

        self._algorithm = algorithm
        self._expiration_seconds = expiration_seconds

    @property
    def algorithm(self) -> str:
        """Return the configured JWT algorithm."""
        return self._algorithm

    def build_claims(
        self,
        subject: str,
        **claims: Any,
    ) -> JWTClaims:
        """Create a JWTClaims object."""
        expires_at = datetime.now(UTC) + timedelta(
            seconds=self._expiration_seconds
        )

        return JWTClaims(
            subject=subject,
            expires_at=expires_at,
            additional_claims=claims,
        )

    def encode(self, claims: JWTClaims, secret: str) -> str:
        """
        Encode JWT claims.

        This method is intended to be implemented by a concrete backend.
        """
        raise NotImplementedError(
            "JWT encoding requires a concrete backend implementation."
        )

    def decode(self, token: str, secret: str) -> JWTClaims:
        """
        Decode a JWT token.

        This method is intended to be implemented by a concrete backend.
        """
        raise JWTDecodeError(
            "JWT decoding requires a concrete backend implementation."
        )