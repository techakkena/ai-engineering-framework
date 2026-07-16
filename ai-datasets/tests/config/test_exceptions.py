"""
Unit tests for ai_datasets.config.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.config.exceptions import (
    ConfigExportError,
    ConfigLoadError,
    ConfigNotFoundError,
    ConfigProviderError,
    ConfigUpdateError,
    ConfigValidationError,
    DatasetConfigError,
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
    exception_class: type[DatasetConfigError],
) -> None:
    """Every custom exception should inherit from DatasetConfigError."""
    assert issubclass(
        exception_class,
        DatasetConfigError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetConfigError,
        match="configuration failure",
    ):
        raise DatasetConfigError(
            "configuration failure",
        )