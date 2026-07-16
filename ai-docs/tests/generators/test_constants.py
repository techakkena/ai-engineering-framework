"""Tests for ai_docs.generators.constants."""

from __future__ import annotations

from ai_docs.generators import constants


def test_default_values() -> None:
    assert constants.DEFAULT_GENERATOR_NAME == "generator"
    assert constants.DEFAULT_GENERATOR_TYPE == "markdown"
    assert constants.DEFAULT_ENABLED is True


def test_supported_generator_types() -> None:
    assert constants.SUPPORTED_GENERATOR_TYPES == frozenset(
        {
            "markdown",
            "openapi",
            "html",
            "pdf",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_GENERATOR_NAME_LENGTH == 3
    assert constants.MAX_GENERATOR_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"