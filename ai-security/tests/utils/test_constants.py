"""
Tests for ai_security.utils.constants.
"""

from ai_security.utils.constants import (
    DEFAULT_ENCODING,
    MASK_CHARACTER,
    TOKEN_PREFIX,
)


def test_default_encoding() -> None:
    """Test the default encoding."""
    assert DEFAULT_ENCODING == "utf-8"


def test_mask_character() -> None:
    """Test the mask character."""
    assert MASK_CHARACTER == "*"


def test_token_prefix() -> None:
    """Test the default token prefix."""
    assert TOKEN_PREFIX == "Bearer"