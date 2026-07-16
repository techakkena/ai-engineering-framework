"""
Unit tests for ai_datasets.config.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.config.exceptions import (
    ConfigValidationError,
)
from ai_datasets.config.operations import (
    ConfigResult,
    export_config,
    get_config,
    load_config,
    reset_config,
    update_config,
)


def test_load_config_success() -> None:
    """Loading a configuration should succeed."""
    result = load_config()

    assert isinstance(result, ConfigResult)
    assert result.success is True
    assert result.task == "load_config"


def test_load_config_empty_name() -> None:
    """Empty configuration names should raise."""
    with pytest.raises(ConfigValidationError):
        load_config("")


def test_get_config_success() -> None:
    """Getting a configuration should succeed."""
    result = get_config("default")

    assert result.success is True
    assert result.task == "get_config"


def test_update_config_success() -> None:
    """Updating a configuration should succeed."""
    result = update_config(
        "default",
        {"key": "value"},
    )

    assert result.success is True
    assert result.task == "update_config"


def test_reset_config_success() -> None:
    """Resetting a configuration should succeed."""
    result = reset_config("default")

    assert result.success is True
    assert result.task == "reset_config"


def test_export_config_success() -> None:
    """Exporting a configuration should succeed."""
    result = export_config("default")

    assert result.success is True
    assert result.task == "export_config"


@pytest.mark.parametrize(
    "operation",
    [
        get_config,
        reset_config,
        export_config,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """All name-based operations should reject empty names."""
    with pytest.raises(ConfigValidationError):
        operation("")


def test_update_config_empty_name() -> None:
    """Updating with an empty configuration name should raise."""
    with pytest.raises(ConfigValidationError):
        update_config(
            "",
            {},
        )