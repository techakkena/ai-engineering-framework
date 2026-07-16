"""Tests for ai_docs.templates.operations."""

from __future__ import annotations

import pytest

from ai_docs.templates.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TEMPLATE_TYPE,
)
from ai_docs.templates.exceptions import (
    DuplicateTemplateError,
    TemplateNotFoundError,
    TemplateValidationError,
    UnsupportedTemplateTypeError,
)
from ai_docs.templates.operations import (
    TemplateDefinition,
    TemplateRegistry,
    build_template,
)


def test_template_defaults() -> None:
    template = TemplateDefinition(
        name="default",
        content="{{ value }}",
    )

    assert template.name == "default"
    assert template.content == "{{ value }}"
    assert template.template_type == DEFAULT_TEMPLATE_TYPE
    assert template.description == ""
    assert template.enabled is DEFAULT_ENABLED


def test_template_trims_name() -> None:
    template = TemplateDefinition(
        name="  default  ",
        content="content",
    )

    assert template.name == "default"


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
        TemplateValidationError,
    ):
        TemplateDefinition(
            name=name,
            content="content",
        )


@pytest.mark.parametrize(
    "content",
    [
        "",
        "   ",
    ],
)
def test_invalid_content(
    content: str,
) -> None:
    with pytest.raises(
        TemplateValidationError,
    ):
        TemplateDefinition(
            name="default",
            content=content,
        )


def test_invalid_template_type() -> None:
    with pytest.raises(
        UnsupportedTemplateTypeError,
    ):
        TemplateDefinition(
            name="default",
            content="content",
            template_type="jinja2",
        )


def test_build_template() -> None:
    template = build_template(
        name="email",
        content="Hello {{ name }}",
        template_type="email",
        description="Email template",
    )

    assert template.name == "email"
    assert template.content == "Hello {{ name }}"
    assert template.template_type == "email"
    assert template.description == "Email template"


def test_registry_register_and_get() -> None:
    registry = TemplateRegistry()

    template = build_template(
        name="default",
        content="content",
    )

    registry.register(template)

    assert registry.get("default") is template
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = TemplateRegistry()

    template = build_template(
        name="default",
        content="content",
    )

    registry.register(template)

    with pytest.raises(
        DuplicateTemplateError,
    ):
        registry.register(template)


def test_registry_unregister() -> None:
    registry = TemplateRegistry()

    template = build_template(
        name="default",
        content="content",
    )

    registry.register(template)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = TemplateRegistry()

    with pytest.raises(
        TemplateNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = TemplateRegistry()

    with pytest.raises(
        TemplateNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = TemplateRegistry()

    registry.register(
        build_template(
            name="default",
            content="content",
        )
    )
    registry.register(
        build_template(
            name="email",
            content="content",
            template_type="email",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = TemplateRegistry()

    first = build_template(
        name="default",
        content="content",
    )
    second = build_template(
        name="email",
        content="content",
        template_type="email",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = TemplateRegistry()

    assert 123 not in registry