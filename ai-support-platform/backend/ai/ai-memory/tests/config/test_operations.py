from __future__ import annotations

"""Tests for ai_memory.config.operations."""

import pytest

from ai_memory.config.constants import (
    ConfigFormat,
    ConfigScope,
)
from ai_memory.config.exceptions import ConfigValidationError
from ai_memory.config.operations import (
    is_valid_config_format,
    is_valid_config_scope,
    validate_config_format,
    validate_config_scope,
)


def test_validate_config_format() -> None:
    assert validate_config_format("json") is ConfigFormat.JSON


def test_validate_config_scope() -> None:
    assert validate_config_scope("memory") is ConfigScope.MEMORY


@pytest.mark.parametrize(
    ("value", "validator"),
    [
        ("invalid", validate_config_format),
        ("invalid", validate_config_scope),
    ],
)
def test_validation_errors(value: str, validator) -> None:
    with pytest.raises(ConfigValidationError):
        validator(value)


def test_is_valid_config_format() -> None:
    assert is_valid_config_format("toml")
    assert not is_valid_config_format("invalid")


def test_is_valid_config_scope() -> None:
    assert is_valid_config_scope("user")
    assert not is_valid_config_scope("invalid")
