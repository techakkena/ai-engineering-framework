"""Tests for ai_docs.markdown.operations."""

from __future__ import annotations

import pytest

from ai_docs.markdown.constants import (
    DEFAULT_ENABLED,
    DEFAULT_MARKDOWN_FORMAT,
)
from ai_docs.markdown.exceptions import (
    DuplicateMarkdownError,
    MarkdownNotFoundError,
    MarkdownValidationError,
    UnsupportedMarkdownFormatError,
)
from ai_docs.markdown.operations import (
    MarkdownDocument,
    MarkdownRegistry,
    build_markdown,
)


def test_markdown_defaults() -> None:
    document = MarkdownDocument(
        name="guide",
        content="# Guide",
    )

    assert document.name == "guide"
    assert document.content == "# Guide"
    assert (
        document.markdown_format
        == DEFAULT_MARKDOWN_FORMAT
    )
    assert document.enabled is DEFAULT_ENABLED


def test_markdown_trims_name() -> None:
    document = MarkdownDocument(
        name="  guide  ",
        content="# Guide",
    )

    assert document.name == "guide"


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
        MarkdownValidationError,
    ):
        MarkdownDocument(
            name=name,
            content="# Guide",
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
        MarkdownValidationError,
    ):
        MarkdownDocument(
            name="guide",
            content=content,
        )


def test_invalid_markdown_format() -> None:
    with pytest.raises(
        UnsupportedMarkdownFormatError,
    ):
        MarkdownDocument(
            name="guide",
            content="# Guide",
            markdown_format="rst",
        )


def test_build_markdown() -> None:
    document = build_markdown(
        name="guide",
        content="# Guide",
        markdown_format="commonmark",
    )

    assert document.name == "guide"
    assert document.content == "# Guide"
    assert (
        document.markdown_format
        == "commonmark"
    )


def test_registry_register_and_get() -> None:
    registry = MarkdownRegistry()

    document = build_markdown(
        name="guide",
        content="# Guide",
    )

    registry.register(document)

    assert registry.get("guide") is document
    assert registry.exists("guide")
    assert len(registry) == 1
    assert "guide" in registry


def test_registry_duplicate_registration() -> None:
    registry = MarkdownRegistry()

    document = build_markdown(
        name="guide",
        content="# Guide",
    )

    registry.register(document)

    with pytest.raises(
        DuplicateMarkdownError,
    ):
        registry.register(document)


def test_registry_unregister() -> None:
    registry = MarkdownRegistry()

    document = build_markdown(
        name="guide",
        content="# Guide",
    )

    registry.register(document)
    registry.unregister("guide")

    assert len(registry) == 0
    assert not registry.exists("guide")


def test_registry_unregister_missing() -> None:
    registry = MarkdownRegistry()

    with pytest.raises(
        MarkdownNotFoundError,
    ):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = MarkdownRegistry()

    with pytest.raises(
        MarkdownNotFoundError,
    ):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = MarkdownRegistry()

    registry.register(
        build_markdown(
            name="guide",
            content="# Guide",
        )
    )
    registry.register(
        build_markdown(
            name="reference",
            content="# Reference",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = MarkdownRegistry()

    first = build_markdown(
        name="guide",
        content="# Guide",
    )
    second = build_markdown(
        name="reference",
        content="# Reference",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (
        first,
        second,
    )


def test_registry_contains_unknown_type() -> None:
    registry = MarkdownRegistry()

    assert 123 not in registry