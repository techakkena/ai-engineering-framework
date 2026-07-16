"""Tests for ai_enterprise.auditing.constants."""

from __future__ import annotations

from ai_enterprise.auditing import constants


def test_default_values() -> None:
    assert constants.DEFAULT_AUDIT_NAME == "audit"
    assert constants.DEFAULT_AUDIT_LEVEL == "info"
    assert constants.DEFAULT_ENABLED is True


def test_supported_levels() -> None:
    assert constants.SUPPORTED_AUDIT_LEVELS == frozenset(
        {
            "info",
            "warning",
            "error",
            "critical",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_AUDIT_NAME_LENGTH == 3
    assert constants.MAX_AUDIT_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.LEVEL_KEY == "level"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"