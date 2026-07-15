"""
Tests for ai_security.hashing.exceptions.
"""

from ai_security.hashing.exceptions import (
    HashingAlgorithmError,
    HashingConfigurationError,
    HashingError,
    HashVerificationError,
)


def test_hashing_error() -> None:
    """HashingError should derive from Exception."""
    error = HashingError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    """Configuration error should derive from HashingError."""
    error = HashingConfigurationError("config")
    assert isinstance(error, HashingError)


def test_algorithm_error() -> None:
    """Algorithm error should derive from HashingError."""
    error = HashingAlgorithmError("algorithm")
    assert isinstance(error, HashingError)


def test_verification_error() -> None:
    """Verification error should derive from HashingError."""
    error = HashVerificationError("verification")
    assert isinstance(error, HashingError)