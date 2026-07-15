"""
Tests for ai_security.jwt.constants.
"""

from ai_security.jwt.constants import (
    DEFAULT_ALGORITHM,
    DEFAULT_AUDIENCE,
    DEFAULT_EXPIRATION_SECONDS,
    DEFAULT_ISSUER,
    SUPPORTED_ALGORITHMS,
)


def test_default_algorithm() -> None:
    """Default algorithm should be HS256."""
    assert DEFAULT_ALGORITHM == "HS256"


def test_default_expiration_seconds() -> None:
    """Default expiration should be one hour."""
    assert DEFAULT_EXPIRATION_SECONDS == 3600


def test_default_issuer() -> None:
    """Issuer should be configured."""
    assert DEFAULT_ISSUER == "ai-engineering-framework"


def test_default_audience() -> None:
    """Audience should be configured."""
    assert DEFAULT_AUDIENCE == "ai-framework"


def test_supported_algorithms() -> None:
    """Supported algorithms should contain common JWT algorithms."""
    assert "HS256" in SUPPORTED_ALGORITHMS
    assert "HS512" in SUPPORTED_ALGORITHMS
    assert "RS256" in SUPPORTED_ALGORITHMS
    assert "ES256" in SUPPORTED_ALGORITHMS