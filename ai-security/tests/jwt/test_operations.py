"""
Tests for ai_security.jwt.operations.
"""

from datetime import UTC, datetime

import pytest

from ai_security.jwt.exceptions import (
    JWTConfigurationError,
    JWTDecodeError,
)
from ai_security.jwt.operations import (
    JWTClaims,
    JWTService,
)


def test_default_service() -> None:
    """Service should use the default algorithm."""
    service = JWTService()

    assert service.algorithm == "HS256"


def test_invalid_algorithm() -> None:
    """Invalid algorithms should raise an exception."""
    with pytest.raises(JWTConfigurationError):
        JWTService(algorithm="INVALID")


def test_build_claims() -> None:
    """Claims should be built correctly."""
    service = JWTService()

    claims = service.build_claims(
        "user123",
        role="admin",
        tenant="acme",
    )

    assert isinstance(claims, JWTClaims)
    assert claims.subject == "user123"
    assert claims.issuer == "ai-engineering-framework"
    assert claims.audience == "ai-framework"
    assert claims.additional_claims["role"] == "admin"
    assert claims.additional_claims["tenant"] == "acme"
    assert isinstance(claims.expires_at, datetime)
    assert claims.expires_at > datetime.now(UTC)


def test_custom_expiration() -> None:
    """Custom expiration should be respected."""
    service = JWTService(expiration_seconds=600)

    claims = service.build_claims("alice")

    assert claims.expires_at is not None
    remaining = (claims.expires_at - datetime.now(UTC)).total_seconds()

    assert remaining <= 600
    assert remaining > 590


def test_encode_not_implemented() -> None:
    """Encoding should require a backend implementation."""
    service = JWTService()

    claims = service.build_claims("user")

    with pytest.raises(NotImplementedError):
        service.encode(claims, "secret")


def test_decode_not_implemented() -> None:
    """Decoding should require a backend implementation."""
    service = JWTService()

    with pytest.raises(JWTDecodeError):
        service.decode("token", "secret")


def test_claims_defaults() -> None:
    """JWTClaims should expose default values."""
    claims = JWTClaims(subject="john")

    assert claims.subject == "john"
    assert claims.additional_claims == {}
    assert claims.expires_at is None


def test_multiple_claims() -> None:
    """Additional claims should be preserved."""
    service = JWTService()

    claims = service.build_claims(
        "user",
        email="user@example.com",
        scope=["read", "write"],
        active=True,
    )

    assert claims.additional_claims["email"] == "user@example.com"
    assert claims.additional_claims["scope"] == ["read", "write"]
    assert claims.additional_claims["active"] is True