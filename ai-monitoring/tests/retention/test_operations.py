"""
Unit tests for ai_monitoring.retention.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.retention.constants import TIME_BASED
from ai_monitoring.retention.exceptions import (
    RetentionValidationError,
)
from ai_monitoring.retention.operations import (
    RetentionResult,
    apply_retention_policy,
    create_retention_policy,
    delete_retention_policy,
    get_retention_policy,
    list_retention_policies,
)


def test_create_retention_policy_success() -> None:
    """Creating a retention policy should succeed."""
    result = create_retention_policy("default")

    assert isinstance(result, RetentionResult)
    assert result.success is True
    assert result.task == "create_retention_policy"
    assert result.data["type"] == TIME_BASED


def test_create_retention_policy_empty_name() -> None:
    """Empty retention policy names should raise."""
    with pytest.raises(RetentionValidationError):
        create_retention_policy("")


def test_apply_retention_policy_success() -> None:
    """Applying a retention policy should succeed."""
    result = apply_retention_policy("default")

    assert result.success is True
    assert result.task == "apply_retention_policy"


def test_get_retention_policy_success() -> None:
    """Getting a retention policy should succeed."""
    result = get_retention_policy("default")

    assert result.success is True
    assert result.task == "get_retention_policy"


def test_delete_retention_policy_success() -> None:
    """Deleting a retention policy should succeed."""
    result = delete_retention_policy("default")

    assert result.success is True
    assert result.task == "delete_retention_policy"


def test_list_retention_policies_success() -> None:
    """Listing retention policies should succeed."""
    result = list_retention_policies()

    assert result.success is True
    assert result.task == "list_retention_policies"
    assert isinstance(result.data["policies"], list)


@pytest.mark.parametrize(
    "operation",
    [
        apply_retention_policy,
        get_retention_policy,
        delete_retention_policy,
    ],
)
def test_name_validation(
    operation,
) -> None:
    """Operations requiring a policy name should reject empty values."""
    with pytest.raises(RetentionValidationError):
        operation("")