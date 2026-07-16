"""Tests for ai_plugins.lifecycle.constants."""

from __future__ import annotations

from ai_plugins.lifecycle import constants


def test_default_values() -> None:
    assert constants.DEFAULT_LIFECYCLE_NAME == "lifecycle"
    assert constants.DEFAULT_PHASE == "initialize"
    assert constants.DEFAULT_ENABLED is True


def test_supported_lifecycle_phases() -> None:
    assert constants.SUPPORTED_LIFECYCLE_PHASES == frozenset(
        {
            "initialize",
            "start",
            "stop",
            "destroy",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_LIFECYCLE_NAME_LENGTH == 1
    assert constants.MAX_LIFECYCLE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.PHASE_KEY == "phase"
    assert constants.ORDER_KEY == "order"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"