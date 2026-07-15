"""
Tests for ai_security.utils.exceptions.
"""

from ai_security.utils.exceptions import (
    SecurityUtilityError,
    ValidationError,
)


def test_security_utility_error() -> None:
    """SecurityUtilityError should derive from Exception."""
    error = SecurityUtilityError("utility error")

    assert str(error) == "utility error"


def test_validation_error() -> None:
    """ValidationError should derive from SecurityUtilityError."""
    error = ValidationError("validation error")

    assert isinstance(error, SecurityUtilityError)