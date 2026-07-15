"""
Tests for ai_security.jwt.exceptions.
"""

from ai_security.jwt.exceptions import (
    JWTConfigurationError,
    JWTDecodeError,
    JWTEncodeError,
    JWTError,
    JWTValidationError,
)


def test_jwt_error() -> None:
    """JWTError should derive from Exception."""
    error = JWTError("error")
    assert str(error) == "error"


def test_configuration_error() -> None:
    """JWTConfigurationError should derive from JWTError."""
    error = JWTConfigurationError("configuration")
    assert isinstance(error, JWTError)


def test_encode_error() -> None:
    """JWTEncodeError should derive from JWTError."""
    error = JWTEncodeError("encode")
    assert isinstance(error, JWTError)


def test_decode_error() -> None:
    """JWTDecodeError should derive from JWTError."""
    error = JWTDecodeError("decode")
    assert isinstance(error, JWTError)


def test_validation_error() -> None:
    """JWTValidationError should derive from JWTError."""
    error = JWTValidationError("validation")
    assert isinstance(error, JWTError)