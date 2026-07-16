"""Tests for ai_analytics.aggregation.operations."""

from __future__ import annotations

import pytest

from ai_analytics.aggregation.constants import (
    DEFAULT_AGGREGATION_TYPE,
    DEFAULT_ENABLED,
)
from ai_analytics.aggregation.exceptions import (
    AggregationNotFoundError,
    AggregationValidationError,
    DuplicateAggregationError,
    UnsupportedAggregationTypeError,
)
from ai_analytics.aggregation.operations import (
    AggregationDefinition,
    AggregationRegistry,
    build_aggregation,
)


def test_aggregation_definition_defaults() -> None:
    aggregation = AggregationDefinition(
        name="total",
        field="amount",
    )

    assert aggregation.name == "total"
    assert aggregation.field == "amount"
    assert aggregation.aggregation_type == (
        DEFAULT_AGGREGATION_TYPE
    )
    assert aggregation.description == ""
    assert aggregation.enabled is DEFAULT_ENABLED


def test_aggregation_definition_trims_values() -> None:
    aggregation = AggregationDefinition(
        name="  total  ",
        field="  amount  ",
    )

    assert aggregation.name == "total"
    assert aggregation.field == "amount"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(AggregationValidationError):
        AggregationDefinition(
            name=name,
            field="amount",
        )


@pytest.mark.parametrize(
    "field",
    [
        "",
        "   ",
    ],
)
def test_invalid_field(field: str) -> None:
    with pytest.raises(AggregationValidationError):
        AggregationDefinition(
            name="total",
            field=field,
        )


def test_invalid_aggregation_type() -> None:
    with pytest.raises(
        UnsupportedAggregationTypeError,
    ):
        AggregationDefinition(
            name="total",
            field="amount",
            aggregation_type="median",
        )


def test_build_aggregation() -> None:
    aggregation = build_aggregation(
        name="average",
        field="score",
        aggregation_type="average",
        description="Average score",
    )

    assert aggregation.name == "average"
    assert aggregation.field == "score"
    assert aggregation.aggregation_type == "average"
    assert aggregation.description == "Average score"


def test_registry_register_and_get() -> None:
    registry = AggregationRegistry()

    aggregation = build_aggregation(
        name="total",
        field="amount",
    )

    registry.register(aggregation)

    assert registry.get("total") is aggregation
    assert registry.exists("total")
    assert len(registry) == 1
    assert "total" in registry


def test_registry_duplicate_registration() -> None:
    registry = AggregationRegistry()

    aggregation = build_aggregation(
        name="total",
        field="amount",
    )

    registry.register(aggregation)

    with pytest.raises(DuplicateAggregationError):
        registry.register(aggregation)


def test_registry_unregister() -> None:
    registry = AggregationRegistry()

    aggregation = build_aggregation(
        name="total",
        field="amount",
    )

    registry.register(aggregation)
    registry.unregister("total")

    assert len(registry) == 0
    assert not registry.exists("total")


def test_registry_unregister_missing() -> None:
    registry = AggregationRegistry()

    with pytest.raises(AggregationNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = AggregationRegistry()

    with pytest.raises(AggregationNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = AggregationRegistry()

    registry.register(
        build_aggregation(
            name="one",
            field="field1",
        )
    )
    registry.register(
        build_aggregation(
            name="two",
            field="field2",
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = AggregationRegistry()

    first = build_aggregation(
        name="one",
        field="field1",
    )
    second = build_aggregation(
        name="two",
        field="field2",
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = AggregationRegistry()

    assert 123 not in registry