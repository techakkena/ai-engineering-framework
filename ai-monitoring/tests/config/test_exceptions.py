"""
Unit tests for ai_monitoring.config.exceptions.
"""

from __future__ import annotations

import pytest

from ai_monitoring.config.exceptions import (
    ConfigExportError,
    ConfigLoadError,
    ConfigNotFoundError,
    ConfigProviderError,
    ConfigUpdateError,
    ConfigValidationError,
    MonitoringConfigError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        ConfigValidationError,
        ConfigNotFoundError,
        ConfigLoadError,
        ConfigUpdateError,
        ConfigExportError,
        ConfigProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[MonitoringConfigError],
) -> None:
    """Every custom exception should inherit from MonitoringConfigError."""
    assert issubclass(
        exception_class,
        MonitoringConfigError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        MonitoringConfigError,
        match="configuration failure",
    ):
        raise MonitoringConfigError(
            "configuration failure",
        )