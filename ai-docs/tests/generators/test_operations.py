"""Tests for ai_docs.generators.operations."""

from __future__ import annotations

import pytest

from ai_docs.generators.constants import (
    DEFAULT_ENABLED,
    DEFAULT_GENERATOR_TYPE,
)
from ai_docs.generators.exceptions import (
    DuplicateGeneratorError,
    GeneratorNotFoundError,
    GeneratorValidationError,
    UnsupportedGeneratorTypeError,
)
from ai_docs.generators.operations import (
    DocumentationGenerator,
    GeneratorRegistry,
    build_generator,
)


def test_generator_defaults() -> None:
    generator = DocumentationGenerator(
        name="default",
    )

    assert generator.name == "default"
    assert generator.generator_type == DEFAULT_GENERATOR_TYPE
    assert generator.description == ""
    assert generator.enabled is DEFAULT_ENABLED


def test_generator_trims_name() -> None:
    generator = DocumentationGenerator(
        name="  default  ",
    )

    assert generator.name == "default"


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
        GeneratorValidationError,
    ):
        DocumentationGenerator(
            name=name,
        )


def test_invalid_generator_type() -> None:
    with pytest.raises(
        UnsupportedGeneratorTypeError,
    ):
        DocumentationGenerator(
            name="default",
            generator_type="docx",
        )


def test_build_generator() -> None:
    generator = build_generator(
        name="html",
        generator_type="html",
        description="HTML generator",
    )

    assert generator.name == "html"
    assert generator.generator_type == "html"
    assert generator.description == "HTML generator"


def test_registry_register_and_get() -> None:
    registry = GeneratorRegistry()

    generator = build_generator(
        name="default",
    )

    registry.register(generator)

    assert registry.get("default") is generator
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = GeneratorRegistry()

    generator = build_generator(
        name="default",
    )

    registry.register(generator)

    with pytest.raises(
        DuplicateGeneratorError,
    ):
        registry.register(generator)


def test_registry_unregister() -> None:
    registry = GeneratorRegistry()

    generator = build_generator(
        name="default",
    )

    registry.register(generator)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = GeneratorRegistry()

    with pytest.raises(
        GeneratorNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = GeneratorRegistry()

    with pytest.raises(
        GeneratorNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = GeneratorRegistry()

    registry.register(
        build_generator(
            name="default",
        )
    )
    registry.register(
        build_generator(
            name="html",
            generator_type="html",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = GeneratorRegistry()

    first = build_generator(
        name="default",
    )
    second = build_generator(
        name="html",
        generator_type="html",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = GeneratorRegistry()

    assert 123 not in registry