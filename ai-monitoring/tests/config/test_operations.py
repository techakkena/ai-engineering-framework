"""
Unit tests for ai_monitoring.config.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.config.constants import DEFAULT_CONFIG_NAME
from ai_monitoring.config.exceptions import (
    ConfigValidationError,
)
from ai_monitoring.config.operations import (
    ConfigResult,
    export_config,
    get_config,
    list_configs,
    load_config,
    update_config,
)


def test_load_default_config() -> None:
    """Loading the default configuration should succeed."""
    result = load_config()

    assert isinstance(result, ConfigResult)
    assert result.success is True
    assert result.task == "load_config"
    assert result.data["name"] == DEFAULT_CONFIG_NAME


def test_load_named_config() -> None:
    """Loading a named configuration should succeed."""
    result = load_config("production")

    assert result.success is True
    assert result.data["name"] == "production"


def test_get_config_success() -> None:
    """Getting a configuration should succeed."""
    result = get_config("production")

    assert result.success is True
    assert result.task == "get_config"


def test_update_config_success() -> None:
    """Updating a configuration should succeed."""
    values = {
        "enabled": True,
        "interval": 60,
    }

    result = update_config(
        "production",
        values,
    )

    assert result.success is True
    assert result.task == "update_config"
    assert result.data["values"] == values


def test_export_config_success() -> None:
    """Exporting a configuration should succeed."""
    result = export_config("production")

    assert result.success is True
    assert result.task == "export_config"


def test_list_configs_success() -> None:
    """Listing configurations should succeed."""
    result = list_configs()

    assert result.success is True
    assert result.task == "list_configs"
    assert isinstance(result.data["configs"], list)


@pytest.mark.parametrize(
    "operation",
    [
        load_config,
        get_config,
        export_config,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring configuration names should reject empty values."""
    with pytest.raises(ConfigValidationError):
        operation("")


def test_update_config_empty_name() -> None:
    """Updating with an empty configuration name should raise."""
    with pytest.raises(ConfigValidationError):
        update_config(
            "",
            {},
        )