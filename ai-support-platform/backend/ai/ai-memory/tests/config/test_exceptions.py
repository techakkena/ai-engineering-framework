from __future__ import annotations

"""Tests for ai_memory.config.exceptions."""

from ai_memory.config.exceptions import (
    ConfigError,
    ConfigFormatError,
    ConfigNotFoundError,
    ConfigValidationError,
)


def test_exception_inheritance() -> None:
    assert issubclass(ConfigNotFoundError, ConfigError)
    assert issubclass(ConfigValidationError, ConfigError)
    assert issubclass(ConfigFormatError, ConfigError)


def test_raise_config_not_found_error() -> None:
    try:
        raise ConfigNotFoundError("not found")
    except ConfigNotFoundError as exc:
        assert str(exc) == "not found"


def test_raise_config_validation_error() -> None:
    try:
        raise ConfigValidationError("validation")
    except ConfigValidationError as exc:
        assert str(exc) == "validation"


def test_raise_config_format_error() -> None:
    try:
        raise ConfigFormatError("format")
    except ConfigFormatError as exc:
        assert str(exc) == "format"
