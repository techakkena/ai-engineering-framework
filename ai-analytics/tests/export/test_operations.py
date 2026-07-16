"""Tests for ai_analytics.export.operations."""

from __future__ import annotations

import pytest

from ai_analytics.export.constants import (
    DEFAULT_ENABLED,
    DEFAULT_EXPORT_FORMAT,
)
from ai_analytics.export.exceptions import (
    DuplicateExportError,
    ExportNotFoundError,
    ExportValidationError,
    UnsupportedExportFormatError,
)
from ai_analytics.export.operations import (
    ExportDefinition,
    ExportRegistry,
    build_export,
)


def test_export_definition_defaults() -> None:
    export = ExportDefinition(
        name="daily",
        destination="reports/",
    )

    assert export.name == "daily"
    assert export.destination == "reports/"
    assert export.export_format == DEFAULT_EXPORT_FORMAT
    assert export.description == ""
    assert export.enabled is DEFAULT_ENABLED


def test_export_definition_trims_values() -> None:
    export = ExportDefinition(
        name="  daily  ",
        destination="  reports/  ",
    )

    assert export.name == "daily"
    assert export.destination == "reports/"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(ExportValidationError):
        ExportDefinition(
            name=name,
            destination="reports/",
        )


@pytest.mark.parametrize(
    "destination",
    [
        "",
        "   ",
    ],
)
def test_invalid_destination(
    destination: str,
) -> None:
    with pytest.raises(ExportValidationError):
        ExportDefinition(
            name="daily",
            destination=destination,
        )


def test_invalid_export_format() -> None:
    with pytest.raises(
        UnsupportedExportFormatError,
    ):
        ExportDefinition(
            name="daily",
            destination="reports/",
            export_format="xml",
        )


def test_build_export() -> None:
    export = build_export(
        name="sales",
        destination="exports/",
        export_format="csv",
        description="Sales export",
    )

    assert export.name == "sales"
    assert export.destination == "exports/"
    assert export.export_format == "csv"
    assert export.description == "Sales export"


def test_registry_register_and_get() -> None:
    registry = ExportRegistry()

    export = build_export(
        name="daily",
        destination="reports/",
    )

    registry.register(export)

    assert registry.get("daily") is export
    assert registry.exists("daily")
    assert len(registry) == 1
    assert "daily" in registry


def test_registry_duplicate_registration() -> None:
    registry = ExportRegistry()

    export = build_export(
        name="daily",
        destination="reports/",
    )

    registry.register(export)

    with pytest.raises(DuplicateExportError):
        registry.register(export)


def test_registry_unregister() -> None:
    registry = ExportRegistry()

    export = build_export(
        name="daily",
        destination="reports/",
    )

    registry.register(export)
    registry.unregister("daily")

    assert len(registry) == 0
    assert not registry.exists("daily")


def test_registry_unregister_missing() -> None:
    registry = ExportRegistry()

    with pytest.raises(ExportNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ExportRegistry()

    with pytest.raises(ExportNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ExportRegistry()

    registry.register(
        build_export(
            name="one",
            destination="one/",
        )
    )
    registry.register(
        build_export(
            name="two",
            destination="two/",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ExportRegistry()

    first = build_export(
        name="one",
        destination="one/",
    )
    second = build_export(
        name="two",
        destination="two/",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = ExportRegistry()

    assert 123 not in registry