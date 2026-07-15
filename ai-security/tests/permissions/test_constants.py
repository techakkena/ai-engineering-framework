"""
Tests for ai_security.permissions.constants.
"""

from ai_security.permissions.constants import (
    DEFAULT_ROLE,
    DEFAULT_SEPARATOR,
    WILDCARD_PERMISSION,
)


def test_default_role() -> None:
    """Test the default role."""
    assert DEFAULT_ROLE == "user"


def test_default_separator() -> None:
    """Test the default permission separator."""
    assert DEFAULT_SEPARATOR == ":"


def test_wildcard_permission() -> None:
    """Test the wildcard permission."""
    assert WILDCARD_PERMISSION == "*"