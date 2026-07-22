"""
Unit tests for ai_monitoring.collectors.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.collectors.exceptions import (
    CollectionError,
    CollectorConfigurationError,
    CollectorError,
    CollectorNotFoundError,
    CollectorProviderError,
    CollectorValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        CollectorValidationError,
        CollectorNotFoundError,
        CollectionError,
        CollectorConfigurationError,
        CollectorProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[CollectorError],
) -> None:
    """Every custom exception should inherit from CollectorError."""
    assert issubclass(
        exception_class,
        CollectorError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        CollectorError,
        match="collector failure",
    ):
        raise CollectorError(
            "collector failure",
        )