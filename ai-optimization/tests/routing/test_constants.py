"""Tests for ai_optimization.routing.constants."""

from __future__ import annotations

from ai_optimization.routing import constants


def test_default_values() -> None:
    assert constants.DEFAULT_ROUTE_NAME == "route"
    assert constants.DEFAULT_ROUTING_STRATEGY == "round_robin"
    assert constants.DEFAULT_ENABLED is True


def test_supported_routing_strategies() -> None:
    assert constants.SUPPORTED_ROUTING_STRATEGIES == frozenset(
        {
            "round_robin",
            "least_loaded",
            "weighted",
            "random",
        }
    )


def test_name_limits() -> None:
    assert constants.MIN_ROUTE_NAME_LENGTH == 1
    assert constants.MAX_ROUTE_NAME_LENGTH == 255


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.STRATEGY_KEY == "strategy"
    assert constants.WEIGHT_KEY == "weight"
    assert constants.DESCRIPTION_KEY == "description"
    assert constants.ENABLED_KEY == "enabled"