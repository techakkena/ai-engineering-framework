"""
Unit tests for ai_monitoring.profiling.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.profiling.exceptions import (
    ProfileCollectionError,
    ProfileNotFoundError,
    ProfileValidationError,
    ProfilingConfigurationError,
    ProfilingError,
    ProfilingProviderError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        ProfileValidationError,
        ProfileNotFoundError,
        ProfileCollectionError,
        ProfilingConfigurationError,
        ProfilingProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[ProfilingError],
) -> None:
    """Every custom exception should inherit from ProfilingError."""
    assert issubclass(
        exception_class,
        ProfilingError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        ProfilingError,
        match="profiling failure",
    ):
        raise ProfilingError(
            "profiling failure",
        )