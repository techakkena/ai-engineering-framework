"""
Unit tests for ai_datasets.utils.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.utils.exceptions import (
    DatasetInspectionError,
    DatasetStatisticsError,
    DatasetUtilsError,
    SchemaInferenceError,
    UtilityConfigurationError,
    UtilityProviderError,
    UtilityValidationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        UtilityValidationError,
        DatasetInspectionError,
        SchemaInferenceError,
        DatasetStatisticsError,
        UtilityConfigurationError,
        UtilityProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetUtilsError],
) -> None:
    """Every custom exception should inherit from DatasetUtilsError."""
    assert issubclass(
        exception_class,
        DatasetUtilsError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetUtilsError,
        match="utility failure",
    ):
        raise DatasetUtilsError(
            "utility failure",
        )