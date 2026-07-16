"""Tests for ai_docs.exporters.constants."""

from __future__ import annotations

from ai_docs.exporters import constants


def test_default_values() -> None:
    assert constants.DEFAULT_EXPORT_NAME == "export"
    assert constants.DEFAULT_EXPORT_FORMAT == "markdown"
    assert constants.DEFAULT_ENABLED is True


def test_supported_export_formats() -> None:
    assert constants.SUPPORTED_EXPORT_FORMATS == frozenset(
        {
            "markdown",
            "html",
            "pdf",
            "json",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_EXPORT_NAME_LENGTH == 3
    assert constants.MAX_EXPORT_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.FORMAT_KEY == "format"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"