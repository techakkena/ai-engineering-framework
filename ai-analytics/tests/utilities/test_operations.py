"""Tests for ai_analytics.utilities.operations."""

from __future__ import annotations

import pytest

from ai_analytics.utilities.constants import (
    DEFAULT_CATEGORY,
)
from ai_analytics.utilities.exceptions import (
    UtilityValidationError,
)
from ai_analytics.utilities.operations import (
    AnalyticsMetadata,
    build_metadata,
    normalize_name,
)


def test_metadata_defaults() -> None:
    metadata = AnalyticsMetadata(name="analytics")

    assert metadata.name == "analytics"
    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_name_trimmed() -> None:
    metadata = AnalyticsMetadata(
        name="  analytics  ",
    )

    assert metadata.name == "analytics"


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
        AnalyticsMetadata(name=name)


def test_normalize_name() -> None:
    assert (
        normalize_name("Analytics Report")
        == "analytics_report"
    )


def test_normalize_single_word() -> None:
    assert normalize_name("Metrics") == "metrics"


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
        name="analytics",
        category="reporting",
        tags=("daily", "summary"),
    )

    assert metadata.name == "analytics"
    assert metadata.category == "reporting"
    assert metadata.tags == (
        "daily",
        "summary",
    )


def test_build_metadata_defaults() -> None:
    metadata = build_metadata(
        name="analytics",
    )

    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_not_collected_by_pytest() -> None:
    assert AnalyticsMetadata.__test__ is False