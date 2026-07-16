"""Tests for ai_docs.markdown.constants."""

from __future__ import annotations

from ai_docs.markdown import constants


def test_default_values() -> None:
    assert constants.DEFAULT_MARKDOWN_NAME == "document"
    assert constants.DEFAULT_MARKDOWN_FORMAT == "github"
    assert constants.DEFAULT_ENABLED is True


def test_supported_markdown_formats() -> None:
    assert constants.SUPPORTED_MARKDOWN_FORMATS == frozenset(
        {
            "github",
            "commonmark",
            "gitlab",
            "markdown_extra",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_MARKDOWN_NAME_LENGTH == 3
    assert constants.MAX_MARKDOWN_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.FORMAT_KEY == "format"
    assert constants.CONTENT_KEY == "content"
    assert constants.ENABLED_KEY == "enabled"