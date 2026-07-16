"""Tests for ai_plugins.discovery.constants."""

from __future__ import annotations

from ai_plugins.discovery import constants


def test_default_values() -> None:
    assert constants.DEFAULT_DISCOVERY_NAME == "discovery"
    assert constants.DEFAULT_DISCOVERY_STRATEGY == "filesystem"
    assert constants.DEFAULT_ENABLED is True


def test_supported_discovery_strategies() -> None:
    assert constants.SUPPORTED_DISCOVERY_STRATEGIES == frozenset(
        {
            "filesystem",
            "entry_points",
            "package_scan",
            "manual",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_DISCOVERY_NAME_LENGTH == 1
    assert constants.MAX_DISCOVERY_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.STRATEGY_KEY == "strategy"
    assert constants.PATH_KEY == "path"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"