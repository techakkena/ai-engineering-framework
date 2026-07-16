"""
Unit tests for ai_datasets.transformers.exceptions.
"""

from __future__ import annotations

import pytest

from ai_datasets.transformers.exceptions import (
    BatchTransformationError,
    DatasetPipelineError,
    DatasetTransformationError,
    DatasetTransformerError,
    DatasetTransformerProviderError,
    FilterTransformationError,
    MapTransformationError,
    NormalizationError,
    TransformerValidationError,
    UnsupportedTransformationError,
)


@pytest.mark.parametrize(
    "exception_class",
    [
        TransformerValidationError,
        UnsupportedTransformationError,
        DatasetTransformationError,
        FilterTransformationError,
        MapTransformationError,
        NormalizationError,
        BatchTransformationError,
        DatasetPipelineError,
        DatasetTransformerProviderError,
    ],
)
def test_exception_inheritance(
    exception_class: type[DatasetTransformerError],
) -> None:
    """Every custom exception should inherit from DatasetTransformerError."""
    assert issubclass(
        exception_class,
        DatasetTransformerError,
    )


def test_exception_message() -> None:
    """Exception messages should be preserved."""
    with pytest.raises(
        DatasetTransformerError,
        match="transformer failure",
    ):
        raise DatasetTransformerError(
            "transformer failure",
        )