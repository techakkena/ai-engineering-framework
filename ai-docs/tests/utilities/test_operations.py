"""Tests for ai_docs.utilities.operations."""

from __future__ import annotations

import pytest

from ai_docs.utilities.constants import (
    DEFAULT_AUTHOR,
    DEFAULT_VERSION,
)
from ai_docs.utilities.exceptions import (
    UtilityValidationError,
)
from ai_docs.utilities.operations import (
    DocumentationMetadata,
    build_metadata,
    normalize_name,
)


def test_metadata_defaults() -> None:
    metadata = DocumentationMetadata(
        name="API Guide",
    )

    assert metadata.name == "API Guide"
    assert metadata.version == DEFAULT_VERSION
    assert metadata.author == DEFAULT_AUTHOR
    assert metadata.description == ""


def test_metadata_trims_name() -> None:
    metadata = DocumentationMetadata(
        name="  API Guide  ",
    )

    assert metadata.name == "API Guide"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "a" * 256,
    ],
)
def test_invalid_metadata_name(
    name: str,
) -> None:
    with pytest.raises(
        UtilityValidationError,
    ):
        DocumentationMetadata(
            name=name,
        )


def test_normalize_name() -> None:
    assert (
        normalize_name(
            "  Documentation  ",
        )
        == "Documentation"
    )


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_normalize_name_invalid(
    name: str,
) -> None:
    with pytest.raises(
        UtilityValidationError,
    ):
        normalize_name(name)


def test_build_metadata() -> None:
    metadata = build_metadata(
        name="User Guide",
        version="2.0.0",
        author="OpenAI",
        description="User documentation",
    )

    assert metadata.name == "User Guide"
    assert metadata.version == "2.0.0"
    assert metadata.author == "OpenAI"
    assert metadata.description == "User documentation"