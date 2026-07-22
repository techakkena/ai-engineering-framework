"""
Unit tests for ai_monitoring.profiling.operations.
"""

from __future__ import annotations

import pytest

from ai_monitoring.profiling.exceptions import (
    ProfileValidationError,
)
from ai_monitoring.profiling.operations import (
    ProfileResult,
    get_profile,
    list_profiles,
    reset_profiles,
    start_profile,
    stop_profile,
)


def test_start_profile_success() -> None:
    """Starting a profile should succeed."""
    result = start_profile("cpu-profile")

    assert isinstance(result, ProfileResult)
    assert result.success is True
    assert result.task == "start_profile"


def test_start_profile_empty_name() -> None:
    """Empty profile names should raise."""
    with pytest.raises(ProfileValidationError):
        start_profile("")


def test_stop_profile_success() -> None:
    """Stopping a profile should succeed."""
    result = stop_profile("cpu-profile")

    assert result.success is True
    assert result.task == "stop_profile"


def test_get_profile_success() -> None:
    """Getting a profile should succeed."""
    result = get_profile("cpu-profile")

    assert result.success is True
    assert result.task == "get_profile"


def test_list_profiles_success() -> None:
    """Listing profiles should succeed."""
    result = list_profiles()

    assert result.success is True
    assert result.task == "list_profiles"
    assert isinstance(result.data["profiles"], list)


def test_reset_profiles_success() -> None:
    """Resetting profiles should succeed."""
    result = reset_profiles()

    assert result.success is True
    assert result.task == "reset_profiles"


@pytest.mark.parametrize(
    "operation",
    [
        start_profile,
        stop_profile,
        get_profile,
    ],
)
def test_profile_validation(
    operation,
) -> None:
    """Operations requiring a profile name should reject empty values."""
    with pytest.raises(ProfileValidationError):
        operation("")