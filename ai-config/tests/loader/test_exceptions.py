"""
Unit tests for loader exceptions.

Author: TECHAKKENA
"""

from ai_config.loader.exceptions import (
    ConfigurationNotFoundError,
    ConfigurationParseError,
    LoaderError,
    UnsupportedFormatError,
)


def test_loader_error() -> None:
    """Test LoaderError."""
    exception = LoaderError("loader error")

    assert isinstance(exception, Exception)
    assert str(exception) == "loader error"


def test_unsupported_format_error() -> None:
    """Test UnsupportedFormatError."""
    exception = UnsupportedFormatError("unsupported")

    assert isinstance(exception, LoaderError)


def test_configuration_not_found_error() -> None:
    """Test ConfigurationNotFoundError."""
    exception = ConfigurationNotFoundError("missing")

    assert isinstance(exception, LoaderError)


def test_configuration_parse_error() -> None:
    """Test ConfigurationParseError."""
    exception = ConfigurationParseError("parse error")

    assert isinstance(exception, LoaderError)
