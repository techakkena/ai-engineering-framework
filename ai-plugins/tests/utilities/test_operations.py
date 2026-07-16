"""Tests for ai_plugins.utilities.operations."""

from __future__ import annotations

import pytest

from ai_plugins.utilities.constants import (
    DEFAULT_CATEGORY,
)
from ai_plugins.utilities.exceptions import (
    UtilityValidationError,
)
from ai_plugins.utilities.operations import (
    PluginMetadata,
    build_metadata,
    normalize_name,
)


def test_metadata_defaults() -> None:
    metadata = PluginMetadata(
        name="plugin",
    )

    assert metadata.name == "plugin"
    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_name_trimmed() -> None:
    metadata = PluginMetadata(
        name="  plugin  ",
    )

    assert metadata.name == "plugin"


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
        PluginMetadata(
            name=name,
        )


def test_normalize_name() -> None:
    assert (
        normalize_name(
            "Plugin Manager"
        )
        == "plugin_manager"
    )


def test_normalize_single_word() -> None:
    assert normalize_name(
        "Registry"
    ) == "registry"


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
        name="loader",
        category="runtime",
        tags=(
            "plugins",
            "loading",
        ),
    )

    assert metadata.name == "loader"
    assert metadata.category == "runtime"
    assert metadata.tags == (
        "plugins",
        "loading",
    )


def test_build_metadata_defaults() -> None:
    metadata = build_metadata(
        name="loader",
    )

    assert metadata.category == DEFAULT_CATEGORY
    assert metadata.tags == ()


def test_metadata_not_collected_by_pytest() -> None:
    assert PluginMetadata.__test__ is False