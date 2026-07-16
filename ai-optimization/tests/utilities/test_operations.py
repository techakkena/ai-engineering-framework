"""Tests for ai_optimization.utilities.operations."""

from __future__ import annotations

import pytest

from ai_optimization.utilities.constants import (
    DEFAULT_CATEGORY,
)
from ai_optimization.utilities.exceptions import (
    UtilityValidationError,
)
from ai_optimization.utilities.operations import (
    OptimizationMetadata,
    build_metadata,
    normalize_name,
)


def test_metadata_defaults() -> None:
    metadata = OptimizationMetadata(
        name="optimization",
    )

    assert metadata.name == "optimization"
    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_name_trimmed() -> None:
    metadata = OptimizationMetadata(
        name="  optimization  ",
    )

    assert metadata.name == "optimization"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_metadata_name(
    name: str,
) -> None:
    with pytest.raises(
        UtilityValidationError,
    ):
        OptimizationMetadata(
            name=name,
        )


def test_normalize_name() -> None:
    assert (
        normalize_name(
            "Optimization Pipeline"
        )
        == "optimization_pipeline"
    )


def test_normalize_single_word() -> None:
    assert normalize_name(
        "Caching"
    ) == "caching"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_normalize_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        UtilityValidationError,
    ):
        normalize_name(name)


def test_build_metadata() -> None:
    metadata = build_metadata(
        name="optimizer",
        category="performance",
        tags=(
            "cache",
            "routing",
        ),
    )

    assert metadata.name == "optimizer"
    assert metadata.category == "performance"
    assert metadata.tags == (
        "cache",
        "routing",
    )


def test_build_metadata_defaults() -> None:
    metadata = build_metadata(
        name="optimizer",
    )

    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_not_collected_by_pytest() -> None:
    assert OptimizationMetadata.__test__ is False