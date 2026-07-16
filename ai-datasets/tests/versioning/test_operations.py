"""
Unit tests for ai_datasets.versioning.operations.
"""

from __future__ import annotations

import pytest

from ai_datasets.versioning.exceptions import (
    VersionValidationError,
)
from ai_datasets.versioning.operations import (
    VersionResult,
    compare_versions,
    create_version,
    get_version,
    list_versions,
    rollback_version,
)


def test_create_version_success() -> None:
    """Creating a version should succeed."""
    result = create_version()

    assert isinstance(result, VersionResult)
    assert result.success is True
    assert result.task == "create_version"


def test_create_version_empty() -> None:
    """Empty versions should raise."""
    with pytest.raises(VersionValidationError):
        create_version("")


def test_get_version_success() -> None:
    """Getting a version should succeed."""
    result = get_version("1.0.0")

    assert result.success is True
    assert result.task == "get_version"


def test_list_versions_success() -> None:
    """Listing versions should succeed."""
    result = list_versions()

    assert result.success is True
    assert result.task == "list_versions"
    assert isinstance(result.data["versions"], list)


def test_compare_versions_success() -> None:
    """Comparing versions should succeed."""
    result = compare_versions(
        "1.0.0",
        "2.0.0",
    )

    assert result.success is True
    assert result.task == "compare_versions"


def test_compare_versions_invalid() -> None:
    """Empty versions should raise."""
    with pytest.raises(VersionValidationError):
        compare_versions(
            "",
            "2.0.0",
        )


def test_rollback_version_success() -> None:
    """Rollback should succeed."""
    result = rollback_version("1.0.0")

    assert result.success is True
    assert result.task == "rollback_version"


def test_rollback_version_invalid() -> None:
    """Rollback with an empty version should raise."""
    with pytest.raises(VersionValidationError):
        rollback_version("")