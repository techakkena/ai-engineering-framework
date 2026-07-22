"""
Unit tests for ai_monitoring.collectors.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.collectors.constants import CUSTOM
from ai_monitoring.collectors.exceptions import (
    CollectorValidationError,
)
from ai_monitoring.collectors.operations import (
    CollectorResult,
    collect_data,
    get_collector,
    list_collectors,
    register_collector,
    remove_collector,
)


def test_register_collector_success() -> None:
    """Registering a collector should succeed."""
    result = register_collector("system")

    assert isinstance(result, CollectorResult)
    assert result.success is True
    assert result.task == "register_collector"
    assert result.data["type"] == CUSTOM


def test_register_collector_empty_name() -> None:
    """Empty collector names should raise."""
    with pytest.raises(CollectorValidationError):
        register_collector("")


def test_collect_data_success() -> None:
    """Collecting data should succeed."""
    result = collect_data("system")

    assert result.success is True
    assert result.task == "collect_data"


def test_get_collector_success() -> None:
    """Getting a collector should succeed."""
    result = get_collector("system")

    assert result.success is True
    assert result.task == "get_collector"


def test_remove_collector_success() -> None:
    """Removing a collector should succeed."""
    result = remove_collector("system")

    assert result.success is True
    assert result.task == "remove_collector"


def test_list_collectors_success() -> None:
    """Listing collectors should succeed."""
    result = list_collectors()

    assert result.success is True
    assert result.task == "list_collectors"
    assert isinstance(result.data["collectors"], list)


@pytest.mark.parametrize(
    "operation",
    [
        collect_data,
        get_collector,
        remove_collector,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a collector name should reject empty values."""
    with pytest.raises(CollectorValidationError):
        operation("")