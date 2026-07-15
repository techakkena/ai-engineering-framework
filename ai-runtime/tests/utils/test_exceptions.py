"""
Unit tests for ai_runtime.utils.exceptions.
"""

from __future__ import annotations

import pytest

from ai_runtime.utils.exceptions import (
    InvalidEncodingError,
    InvalidUtilityOperationError,
    RuntimeUtilityError,
    UtilityConfigurationError,
)


def test_runtime_utility_error_default_message() -> None:
    """Test RuntimeUtilityError."""
    error = RuntimeUtilityError()

    assert (
        str(error)
        == "A runtime utility error occurred."
    )


def test_runtime_utility_error_custom_message() -> None:
    """Test RuntimeUtilityError custom message."""
    error = RuntimeUtilityError(
        "Custom utility error.",
    )

    assert str(error) == "Custom utility error."


@pytest.mark.parametrize(
    "encoding",
    [
        "",
        "utf-64",
        "ansi",
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
        RuntimeUtilityError,
    )

    assert error.encoding == encoding

    assert (
        str(error)
        == f"Invalid encoding: '{encoding}'."
    )


@pytest.mark.parametrize(
    "operation",
    [
        "encode",
        "decode",
        "serialize",
    ],
)
def test_invalid_utility_operation_error(
    operation: str,
) -> None:
    """Test InvalidUtilityOperationError."""
    error = InvalidUtilityOperationError(
        operation,
    )

    assert isinstance(
        error,
        RuntimeUtilityError,
    )

    assert error.operation == operation

    assert (
        str(error)
        == (
            f"Invalid utility operation: "
            f"'{operation}'."
        )
    )


def test_utility_configuration_error() -> None:
    """Test UtilityConfigurationError."""
    configuration = "encoding"

    error = UtilityConfigurationError(
        configuration,
    )

    assert isinstance(
        error,
        RuntimeUtilityError,
    )

    assert error.configuration == configuration

    assert (
        str(error)
        == (
            "Invalid utility configuration: "
            f"'{configuration}'."
        )
    )