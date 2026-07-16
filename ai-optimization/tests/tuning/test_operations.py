"""Tests for ai_optimization.tuning.operations."""

from __future__ import annotations

import pytest

from ai_optimization.tuning.constants import (
    DEFAULT_ENABLED,
    DEFAULT_TUNING_STRATEGY,
)
from ai_optimization.tuning.exceptions import (
    DuplicateTuningError,
    TuningNotFoundError,
    TuningValidationError,
    UnsupportedTuningStrategyError,
)
from ai_optimization.tuning.operations import (
    TuningDefinition,
    TuningRegistry,
    build_tuning,
)


def test_tuning_definition_defaults() -> None:
    tuning = TuningDefinition(
        name="default",
        iterations=100,
    )

    assert tuning.name == "default"
    assert tuning.iterations == 100
    assert tuning.strategy == DEFAULT_TUNING_STRATEGY
    assert tuning.description == ""
    assert tuning.enabled is DEFAULT_ENABLED


def test_tuning_definition_trims_name() -> None:
    tuning = TuningDefinition(
        name="  default  ",
        iterations=100,
    )

    assert tuning.name == "default"


@pytest.mark.parametrize(
    "name",
    [
        "",
        "   ",
        "a" * 256,
    ],
)
def test_invalid_name(name: str) -> None:
    with pytest.raises(TuningValidationError):
        TuningDefinition(
            name=name,
            iterations=100,
        )


@pytest.mark.parametrize(
    "iterations",
    [
        0,
        -1,
        -100,
    ],
)
def test_invalid_iterations(
    iterations: int,
) -> None:
    with pytest.raises(TuningValidationError):
        TuningDefinition(
            name="default",
            iterations=iterations,
        )


def test_invalid_strategy() -> None:
    with pytest.raises(
        UnsupportedTuningStrategyError,
    ):
        TuningDefinition(
            name="default",
            iterations=100,
            strategy="manual",
        )


def test_build_tuning() -> None:
    tuning = build_tuning(
        name="bayes",
        iterations=250,
        strategy="bayesian",
        description="Bayesian optimization",
    )

    assert tuning.name == "bayes"
    assert tuning.iterations == 250
    assert tuning.strategy == "bayesian"
    assert tuning.description == "Bayesian optimization"


def test_registry_register_and_get() -> None:
    registry = TuningRegistry()

    tuning = build_tuning(
        name="default",
        iterations=100,
    )

    registry.register(tuning)

    assert registry.get("default") is tuning
    assert registry.exists("default")
    assert len(registry) == 1
    assert "default" in registry


def test_registry_duplicate_registration() -> None:
    registry = TuningRegistry()

    tuning = build_tuning(
        name="default",
        iterations=100,
    )

    registry.register(tuning)

    with pytest.raises(DuplicateTuningError):
        registry.register(tuning)


def test_registry_unregister() -> None:
    registry = TuningRegistry()

    tuning = build_tuning(
        name="default",
        iterations=100,
    )

    registry.register(tuning)
    registry.unregister("default")

    assert len(registry) == 0
    assert not registry.exists("default")


def test_registry_unregister_missing() -> None:
    registry = TuningRegistry()

    with pytest.raises(TuningNotFoundError):
        registry.unregister("missing")


def test_registry_get_missing() -> None:
    registry = TuningRegistry()

    with pytest.raises(TuningNotFoundError):
        registry.get("missing")


def test_registry_clear() -> None:
    registry = TuningRegistry()

    registry.register(
        build_tuning(
            name="one",
            iterations=10,
        )
    )
    registry.register(
        build_tuning(
            name="two",
            iterations=20,
        )
    )

    registry.clear()

    assert len(registry) == 0
    assert registry.list() == ()


def test_registry_list() -> None:
    registry = TuningRegistry()

    first = build_tuning(
        name="one",
        iterations=10,
    )
    second = build_tuning(
        name="two",
        iterations=20,
    )

    registry.register(first)
    registry.register(second)

    assert registry.list() == (first, second)


def test_registry_contains_unknown_type() -> None:
    registry = TuningRegistry()

    assert 123 not in registry