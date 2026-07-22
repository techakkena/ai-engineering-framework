"""
Unit tests for ai_monitoring.retention.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.retention.exceptions import (
    RetentionConfigurationError,
    RetentionError,
    RetentionPolicyError,
    RetentionPolicyNotFoundError,
    RetentionProviderError,
    RetentionValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        RetentionValidationError,
        RetentionPolicyNotFoundError,
        RetentionPolicyError,
        RetentionConfigurationError,
        RetentionProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[RetentionError],
) -> None:
    """Every custom exception should inherit from RetentionError."""
    assert issubclass(
        exception_class,
        RetentionError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        RetentionError,
        match="retention failure",
    ):
        raise RetentionError(
            "retention failure",
        )