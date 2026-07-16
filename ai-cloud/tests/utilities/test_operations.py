"""Tests for ai_cloud.utilities.operations."""

from __future__ import annotations

import pytest

from ai_cloud.utilities.constants import (
    DEFAULT_CATEGORY,
)
from ai_cloud.utilities.exceptions import (
    UtilityValidationError,
)
from ai_cloud.utilities.operations import (
    CloudMetadata,
    build_metadata,
    normalize_name,
)


def test_metadata_defaults() -> None:
    metadata = CloudMetadata(
        name="cloud",
    )

    assert metadata.name == "cloud"
    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_name_trimmed() -> None:
    metadata = CloudMetadata(
        name="  cloud  ",
    )

    assert metadata.name == "cloud"


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
        CloudMetadata(
            name=name,
        )


def test_normalize_name() -> None:
    assert (
        normalize_name(
            "Cloud Storage"
        )
        == "cloud_storage"
    )


def test_normalize_single_word() -> None:
    assert normalize_name(
        "Provider"
    ) == "provider"


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
        name="storage",
        category="services",
        tags=(
            "cloud",
            "storage",
        ),
    )

    assert metadata.name == "storage"
    assert metadata.category == "services"
    assert metadata.tags == (
        "cloud",
        "storage",
    )


def test_build_metadata_defaults() -> None:
    metadata = build_metadata(
        name="storage",
    )

    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_not_collected_by_pytest() -> None:
    assert CloudMetadata.__test__ is False