"""Tests for ai_docs.templates.constants."""

from __future__ import annotations

from ai_docs.templates import constants


def test_default_values() -> None:
    assert constants.DEFAULT_TEMPLATE_NAME == "template"
    assert constants.DEFAULT_TEMPLATE_TYPE == "markdown"
    assert constants.DEFAULT_ENABLED is True


def test_supported_template_types() -> None:
    assert constants.SUPPORTED_TEMPLATE_TYPES == frozenset(
        {
            "markdown",
            "html",
            "email",
            "prompt",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_TEMPLATE_NAME_LENGTH == 3
    assert constants.MAX_TEMPLATE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.CONTENT_KEY == "content"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"