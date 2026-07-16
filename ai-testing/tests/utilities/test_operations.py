"""Tests for ai_testing.utilities.operations."""

from __future__ import annotations

import pytest

from ai_testing.utilities.constants import DEFAULT_CATEGORY
from ai_testing.utilities.exceptions import UtilityValidationError
from ai_testing.utilities.operations import (
    TestMetadata,
    build_test_metadata,
    normalize_test_name,
)


def test_metadata_defaults() -> None:
    metadata = TestMetadata(name="sample")

    assert metadata.name == "sample"
    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_name_trimmed() -> None:
    metadata = TestMetadata(name="  sample test  ")

    assert metadata.name == "sample test"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_metadata_name(name: str) -> None:
    with pytest.raises(UtilityValidationError):
        TestMetadata(name=name)


def test_normalize_test_name() -> None:
    assert normalize_test_name("My Test Case") == "my_test_case"


def test_normalize_single_word() -> None:
    assert normalize_test_name("Example") == "example"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_normalize_invalid_name(name: str) -> None:
    with pytest.raises(UtilityValidationError):
        normalize_test_name(name)


def test_build_test_metadata() -> None:
    metadata = build_test_metadata(
        name="login test",
        category="integration",
        tags=("api", "auth"),
    )

    assert metadata.name == "login test"
    assert metadata.category == "integration"
    assert metadata.tags == ("api", "auth")


def test_build_test_metadata_defaults() -> None:
    metadata = build_test_metadata(name="sample")

    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()