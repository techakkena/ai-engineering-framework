"""Tests for ai_docs.openapi.operations."""

from __future__ import annotations

import pytest

from ai_docs.openapi.constants import (
    DEFAULT_ENABLED,
    DEFAULT_OPENAPI_VERSION,
)
from ai_docs.openapi.exceptions import (
    DuplicateOpenAPIError,
    OpenAPINotFoundError,
    OpenAPIValidationError,
    UnsupportedOpenAPIVersionError,
)
from ai_docs.openapi.operations import (
    OpenAPIDocument,
    OpenAPIRegistry,
    build_openapi,
)


def test_openapi_defaults() -> None:
    document = OpenAPIDocument(
        name="petstore",
        title="Pet Store API",
    )

    assert document.name == "petstore"
    assert document.title == "Pet Store API"
    assert document.version == DEFAULT_OPENAPI_VERSION
    assert document.description == ""
    assert document.enabled is DEFAULT_ENABLED


def test_openapi_trims_values() -> None:
    document = OpenAPIDocument(
        name="  petstore  ",
        title="  Pet Store API  ",
    )

    assert document.name == "petstore"
    assert document.title == "Pet Store API"


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
        OpenAPIValidationError,
    ):
        OpenAPIDocument(
            name=name,
            title="API",
        )


@pytest.mark.parametrize(
    "title",
    [
        "",
        "   ",
    ],
)
def test_invalid_title(
    title: str,
) -> None:
    with pytest.raises(
        OpenAPIValidationError,
    ):
        OpenAPIDocument(
            name="petstore",
            title=title,
        )


def test_invalid_version() -> None:
    with pytest.raises(
        UnsupportedOpenAPIVersionError,
    ):
        OpenAPIDocument(
            name="petstore",
            title="API",
            version="2.0",
        )


def test_build_openapi() -> None:
    document = build_openapi(
        name="petstore",
        title="Pet Store API",
        version="3.0.3",
        description="Example API",
    )

    assert document.name == "petstore"
    assert document.title == "Pet Store API"
    assert document.version == "3.0.3"
    assert document.description == "Example API"


def test_registry_register_and_get() -> None:
    registry = OpenAPIRegistry()

    document = build_openapi(
        name="petstore",
        title="Pet Store API",
    )

    registry.register(document)

    assert registry.get("petstore") is document
    assert registry.exists("petstore")
    assert len(registry) == 1
    assert "petstore" in registry


def test_registry_duplicate_registration() -> None:
    registry = OpenAPIRegistry()

    document = build_openapi(
        name="petstore",
        title="Pet Store API",
    )

    registry.register(document)

    with pytest.raises(
        DuplicateOpenAPIError,
    ):
        registry.register(document)


def test_registry_unregister() -> None:
    registry = OpenAPIRegistry()

    document = build_openapi(
        name="petstore",
        title="Pet Store API",
    )

    registry.register(document)
    registry.unregister("petstore")

    assert len(registry) == 0
    assert not registry.exists("petstore")


def test_registry_unregister_missing() -> None:
    registry = OpenAPIRegistry()

    with pytest.raises(
        OpenAPINotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = OpenAPIRegistry()

    with pytest.raises(
        OpenAPINotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = OpenAPIRegistry()

    registry.register(
        build_openapi(
            name="petstore",
            title="Pet Store API",
        )
    )
    registry.register(
        build_openapi(
            name="orders",
            title="Orders API",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = OpenAPIRegistry()

    first = build_openapi(
        name="petstore",
        title="Pet Store API",
    )
    second = build_openapi(
        name="orders",
        title="Orders API",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = OpenAPIRegistry()

    assert 123 not in registry