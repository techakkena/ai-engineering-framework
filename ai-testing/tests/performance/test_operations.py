"""Tests for ai_testing.performance.operations."""

from __future__ import annotations

import pytest

from ai_testing.performance.constants import DEFAULT_TIME_UNIT
from ai_testing.performance.exceptions import (
    InvalidIterationCountError,
    UnsupportedTimeUnitError,
)
from ai_testing.performance.operations import (
    PerformanceRunner,
    measure_performance,
)


def _noop() -> None:
    """Do nothing."""


def test_measure_defaults() -> None:
    result = measure_performance(
        name="benchmark",
        operation=_noop,
    )

    assert result.name == "benchmark"
    assert result.iterations == 1
    assert result.time_unit == DEFAULT_TIME_UNIT
    assert result.duration >= 0.0


def test_measure_milliseconds() -> None:
    result = measure_performance(
        name="benchmark",
        operation=_noop,
        time_unit="milliseconds",
    )

    assert result.time_unit == "milliseconds"
    assert result.duration >= 0.0


def test_measure_microseconds() -> None:
    result = measure_performance(
        name="benchmark",
        operation=_noop,
        time_unit="microseconds",
    )

    assert result.time_unit == "microseconds"
    assert result.duration >= 0.0


def test_measure_nanoseconds() -> None:
    result = measure_performance(
        name="benchmark",
        operation=_noop,
        time_unit="nanoseconds",
    )

    assert result.time_unit == "nanoseconds"
    assert result.duration >= 0.0


@pytest.mark.parametrize(
    "iterations",
    [
        0,
        -1,
        1_000_001,
    ],
)
def test_invalid_iteration_count(
    iterations: int,
) -> None:
    with pytest.raises(InvalidIterationCountError):
        measure_performance(
            name="benchmark",
            operation=_noop,
            iterations=iterations,
        )


def test_invalid_time_unit() -> None:
    with pytest.raises(UnsupportedTimeUnitError):
        measure_performance(
            name="benchmark",
            operation=_noop,
            time_unit="minutes",
        )


def test_runner_measure() -> None:
    runner = PerformanceRunner()

    result = runner.measure(
        name="runner",
        operation=_noop,
        iterations=5,
    )

    assert result.name == "runner"
    assert result.iterations == 5
    assert result.duration >= 0.0


def test_runner_trims_name() -> None:
    runner = PerformanceRunner()

    result = runner.measure(
        name="  benchmark  ",
        operation=_noop,
    )

    assert result.name == "benchmark"