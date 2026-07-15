"""
Tests for ai_security.secrets.constants.
"""

from ai_security.secrets.constants import (
    DEFAULT_SECRET_ENCODING,
    DEFAULT_SECRET_LENGTH,
    DEFAULT_TOKEN_LENGTH,
)


def test_default_secret_length() -> None:
    """Default secret length should be positive."""
    assert DEFAULT_SECRET_LENGTH == 32


def test_default_token_length() -> None:
    """Default token length should be positive."""
    assert DEFAULT_TOKEN_LENGTH == 32


def test_default_secret_encoding() -> None:
    """Default secret encoding should be UTF-8."""
    assert DEFAULT_SECRET_ENCODING == "utf-8"