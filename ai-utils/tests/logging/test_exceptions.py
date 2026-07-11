"""
Unit tests for logging exceptions.
"""

from __future__ import annotations

import pytest

from ai_utils.logging.exceptions import (
    LoggerCreationError,
    LoggingConfigurationError,
    LoggingError,
)


def test_logging_error_is_exception() -> None:
    """LoggingError should inherit from Exception."""
    assert issubclass(LoggingError, Exception)


def test_logging_configuration_error_inherits_logging_error() -> None:
    """LoggingConfigurationError should inherit from LoggingError."""
    assert issubclass(LoggingConfigurationError, LoggingError)


def test_logger_creation_error_inherits_logging_error() -> None:
    """LoggerCreationError should inherit from LoggingError."""
    assert issubclass(LoggerCreationError, LoggingError)


def test_logging_error_message() -> None:
    """LoggingError should preserve its message."""
    message = "Logging failed"
    error = LoggingError(message)

    assert str(error) == message


def test_logging_configuration_error_message() -> None:
    """LoggingConfigurationError should preserve its message."""
    message = "Invalid configuration"
    error = LoggingConfigurationError(message)

    assert str(error) == message


def test_logger_creation_error_message() -> None:
    """LoggerCreationError should preserve its message."""
    message = "Unable to create logger"
    error = LoggerCreationError(message)

    assert str(error) == message


@pytest.mark.parametrize(
    "exception_class",
    [
        LoggingError,
        LoggingConfigurationError,
        LoggerCreationError,
    ],
)
def test_exception_can_be_raised(exception_class: type[Exception]) -> None:
    """Each custom exception should be raisable."""
    with pytest.raises(exception_class):
        raise exception_class("Test exception")
