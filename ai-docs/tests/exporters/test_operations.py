"""Tests for ai_docs.exporters.operations."""

from __future__ import annotations

import pytest

from ai_docs.exporters.constants import (
    DEFAULT_ENABLED,
    DEFAULT_EXPORT_FORMAT,
)
from ai_docs.exporters.exceptions import (
    DuplicateExportError,
    ExportNotFoundError,
    ExportValidationError,
    UnsupportedExportFormatError,
)
from ai_docs.exporters.operations import (
    ExportDefinition,
    ExportRegistry,
    build_exporter,
)


def test_export_defaults() -> None:
    export = ExportDefinition(
        name="default",
    )

    assert export.name == "default"
    assert export.export_format == DEFAULT_EXPORT_FORMAT
    assert export.description == ""
    assert export.enabled is DEFAULT_ENABLED


def test_export_trims_name() -> None:
    export = ExportDefinition(
        name="  default  ",
    )

    assert export.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        " ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        ExportValidationError,
    ):
        ExportDefinition(
            name=name,
        )


def test_invalid_export_format() -> None:
    with pytest.raises(
        UnsupportedExportFormatError,
    ):
        ExportDefinition(
            name="default",
            export_format="docx",
        )


def test_build_exporter() -> None:
    export = build_exporter(
        name="pdf",
        export_format="pdf",
        description="PDF exporter",
    )

    assert export.name == "pdf"
    assert export.export_format == "pdf"
    assert export.description == "PDF exporter"


def test_registry_register_and_get() -> None:
    registry = ExportRegistry()

    export = build_exporter(
        name="default",
    )

    registry.register(export)

    assert registry.get("default") is export
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = ExportRegistry()

    export = build_exporter(
        name="default",
    )

    registry.register(export)

    with pytest.raises(
        DuplicateExportError,
    ):
        registry.register(export)


def test_registry_unregister() -> None:
    registry = ExportRegistry()

    export = build_exporter(
        name="default",
    )

    registry.register(export)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = ExportRegistry()

    with pytest.raises(
        ExportNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = ExportRegistry()

    with pytest.raises(
        ExportNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = ExportRegistry()

    registry.register(
        build_exporter(
            name="default",
        )
    )
    registry.register(
        build_exporter(
            name="pdf",
            export_format="pdf",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = ExportRegistry()

    first = build_exporter(
        name="default",
    )
    second = build_exporter(
        name="pdf",
        export_format="pdf",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = ExportRegistry()

    assert 123 not in registry