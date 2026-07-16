"""
Unit tests for ai_datasets.splitters.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.splitters.exceptions import (
    DatasetSplitError,
    DatasetSplitterError,
    KFoldSplitError,
    SplitConfigurationError,
    SplitProviderError,
    SplitValidationError,
    StratifiedSplitError,
    TimeSeriesSplitError,
    TrainTestSplitError,
    UnsupportedSplitStrategyError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        SplitValidationError,
        UnsupportedSplitStrategyError,
        DatasetSplitError,
        TrainTestSplitError,
        StratifiedSplitError,
        KFoldSplitError,
        TimeSeriesSplitError,
        SplitConfigurationError,
        SplitProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetSplitterError],
) -> None:
    """Every custom exception should inherit from DatasetSplitterError."""
    assert issubclass(
        exception_class,
        DatasetSplitterError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetSplitterError,
        match="splitter failure",
    ):
        raise DatasetSplitterError(
            "splitter failure",
        )