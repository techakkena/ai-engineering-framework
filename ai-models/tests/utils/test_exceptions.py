"""
Unit tests for ai_models.utils.exceptions.
"""

from __future__ import annotations

import pytest

from ai_models.utils.exceptions import (
    InvalidEncodingError,
    UtilityConfigurationError,
    UtilityError,
    UtilityValidationError,
)


def test_utility_error_default_message() -> None:
    """Test UtilityError default message."""
    error = UtilityError()

    assert (
        str(error)
        == "A utility error occurred."
    )


def test_utility_error_custom_message() -> None:
    """Test UtilityError custom message."""
    error = UtilityError(
        "Custom utility error.",
    )

    assert (
        str(error)
        == "Custom utility error."
    )


@pytest.mark.parametrize(
    "encoding",
    [
        "",
        "utf-32",
        "cp1252",
    ],
)
def test_invalid_encoding_error(
    encoding: str,
) -> None:
    """Test InvalidEncodingError."""
    error = InvalidEncodingError(
        encoding,
    )

    assert isinstance(
        error,
        UtilityError,
    )

    assert error.encoding == encoding

    assert (
        str(error)
        == (
            "Invalid encoding: "
            f"'{encoding}'."
        )
    )


def test_utility_configuration_error() -> None:
    """Test UtilityConfigurationError."""
    configuration = "timeout"

    error = UtilityConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        UtilityError,
    )

    assert (
        error.configuration
        == configuration
    )

    assert (
        str(error)
        == (
            "Invalid utility "
            "configuration: "
            f"'{configuration}'."
        )
    )


def test_utility_validation_error() -> None:
    """Test UtilityValidationError."""
    value = "gpt@5"
    reason = "invalid characters"

    error = UtilityValidationError(
        value,
        reason,
    )

    assert isinstance(
        error,
        UtilityError,
    )

    assert error.value == value
    assert error.reason == reason

    assert (
        str(error)
        == (
            f"'{value}' "
            f"validation failed: "
            f"{reason}."
        )
    )