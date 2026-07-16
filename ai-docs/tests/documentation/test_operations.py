"""Tests for ai_docs.documentation.operations."""

from __future__ import annotations

import pytest

from ai_docs.documentation.constants import (
    DEFAULT_DOCUMENTATION_TYPE,
    DEFAULT_ENABLED,
)
from ai_docs.documentation.exceptions import (
    DocumentationNotFoundError,
    DocumentationValidationError,
    DuplicateDocumentationError,
    UnsupportedDocumentationTypeError,
)
from ai_docs.documentation.operations import (
    DocumentationDefinition,
    DocumentationRegistry,
    build_documentation,
)


def test_documentation_defaults() -> None:
    documentation = DocumentationDefinition(
        name="api-guide",
    )

    assert documentation.name == "api-guide"
    assert (
        documentation.documentation_type
        == DEFAULT_DOCUMENTATION_TYPE
    )
    assert documentation.description == ""
    assert documentation.enabled is DEFAULT_ENABLED


def test_documentation_trims_name() -> None:
    documentation = DocumentationDefinition(
        name="  api-guide  ",
    )

    assert documentation.name == "api-guide"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "  ",
        "ab",
        "a" * 256,
    ],
)
def test_invalid_name(
    name: str,
) -> None:
    with pytest.raises(
        DocumentationValidationError,
    ):
        DocumentationDefinition(
            name=name,
        )


def test_invalid_documentation_type() -> None:
    with pytest.raises(
        UnsupportedDocumentationTypeError,
    ):
        DocumentationDefinition(
            name="guide",
            documentation_type="docx",
        )


def test_build_documentation() -> None:
    documentation = build_documentation(
        name="api-reference",
        documentation_type="html",
        description="HTML API documentation",
    )

    assert documentation.name == "api-reference"
    assert documentation.documentation_type == "html"
    assert (
        documentation.description
        == "HTML API documentation"
    )


def test_registry_register_and_get() -> None:
    registry = DocumentationRegistry()

    documentation = build_documentation(
        name="guide",
    )

    registry.register(documentation)

    assert registry.get("guide") is documentation
    assert registry.exists("guide")
    assert len(registry) == 1
    assert "guide" in registry


def test_registry_duplicate_registration() -> None:
    registry = DocumentationRegistry()

    documentation = build_documentation(
        name="guide",
    )

    registry.register(documentation)

    with pytest.raises(
        DuplicateDocumentationError,
    ):
        registry.register(documentation)


def test_registry_unregister() -> None:
    registry = DocumentationRegistry()

    documentation = build_documentation(
        name="guide",
    )

    registry.register(documentation)
    registry.unregister("guide")

    assert len(registry) == 0
    assert not registry.exists("guide")


def test_registry_unregister_missing() -> None:
    registry = DocumentationRegistry()

    with pytest.raises(
        DocumentationNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = DocumentationRegistry()

    with pytest.raises(
        DocumentationNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = DocumentationRegistry()

    registry.register(
        build_documentation(
            name="guide",
        )
    )
    registry.register(
        build_documentation(
            name="reference",
            documentation_type="html",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = DocumentationRegistry()

    first = build_documentation(
        name="guide",
    )
    second = build_documentation(
        name="reference",
        documentation_type="html",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = DocumentationRegistry()

    assert 123 not in registry