"""Tests for ai_enterprise.policies.constants."""

from __future__ import annotations

from ai_enterprise.policies import constants


def test_default_values() -> None:
    assert constants.DEFAULT_POLICY_NAME == "default"
    assert constants.DEFAULT_POLICY_TYPE == "access"
    assert constants.DEFAULT_ENABLED is True


def test_supported_policy_types() -> None:
    assert constants.SUPPORTED_POLICY_TYPES == frozenset(
        {
            "access",
            "security",
            "retention",
            "compliance",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_POLICY_NAME_LENGTH == 3
    assert constants.MAX_POLICY_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.TYPE_KEY == "type"
    assert constants.RULES_KEY == "rules"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"