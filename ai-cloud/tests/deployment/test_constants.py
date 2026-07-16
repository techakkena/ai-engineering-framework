"""Tests for ai_cloud.deployment.constants."""

from __future__ import annotations

from ai_cloud.deployment import constants


def test_default_values() -> None:
    assert constants.DEFAULT_DEPLOYMENT_NAME == "deployment"
    assert constants.DEFAULT_DEPLOYMENT_STRATEGY == "rolling"
    assert constants.DEFAULT_ENABLED is True


def test_supported_deployment_strategies() -> None:
    assert constants.SUPPORTED_DEPLOYMENT_STRATEGIES == frozenset(
        {
            "rolling",
            "blue_green",
            "canary",
            "recreate",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_DEPLOYMENT_NAME_LENGTH == 1
    assert constants.MAX_DEPLOYMENT_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.STRATEGY_KEY == "strategy"
    assert constants.REPLICAS_KEY == "replicas"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"