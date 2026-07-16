"""Tests for ai_analytics.reporting.constants."""

from __future__ import annotations

from ai_analytics.reporting import constants


def test_default_values() -> None:
    assert constants.DEFAULT_REPORT_NAME == "report"
    assert constants.DEFAULT_REPORT_FORMAT == "json"
    assert constants.DEFAULT_ENABLED is True


def test_supported_report_formats() -> None:
    assert constants.SUPPORTED_REPORT_FORMATS == frozenset(
        {
            "json",
            "csv",
            "html",
            "pdf",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_REPORT_NAME_LENGTH == 1
    assert constants.MAX_REPORT_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.FORMAT_KEY == "format"
    assert constants.TITLE_KEY == "title"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"