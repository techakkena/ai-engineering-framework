"""Tests for ai_analytics.dashboards.constants."""

from __future__ import annotations

from ai_analytics.dashboards import constants


def test_default_values() -> None:
    assert constants.DEFAULT_DASHBOARD_NAME == "dashboard"
    assert constants.DEFAULT_LAYOUT == "grid"
    assert constants.DEFAULT_ENABLED is True


def test_supported_layouts() -> None:
    assert constants.SUPPORTED_LAYOUTS == frozenset(
        {
            "grid",
            "list",
            "tabs",
            "freeform",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_DASHBOARD_NAME_LENGTH == 1
    assert constants.MAX_DASHBOARD_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TITLE_KEY == "title"
    assert constants.LAYOUT_KEY == "layout"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"