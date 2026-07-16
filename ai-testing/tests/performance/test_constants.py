"""Tests for ai_testing.performance.constants."""

from __future__ import annotations

from ai_testing.performance import constants


def test_default_values() -> None:
    assert constants.DEFAULT_BENCHMARK_NAME == "benchmark"
    assert constants.DEFAULT_ITERATIONS == 1
    assert constants.DEFAULT_WARMUP_ITERATIONS == 0
    assert constants.DEFAULT_TIME_UNIT == "seconds"


def test_iteration_limits() -> None:
    assert constants.MIN_ITERATIONS == 1
    assert constants.MAX_ITERATIONS == 1_000_000


def test_supported_time_units() -> None:
    assert constants.SUPPORTED_TIME_UNITS == frozenset(
        {
            "seconds",
            "milliseconds",
            "microseconds",
            "nanoseconds",
        }
    )


def test_metadata_keys() -> None:
    assert constants.NAME_KEY == "name"
    assert constants.ITERATIONS_KEY == "iterations"
    assert constants.DURATION_KEY == "duration"
    assert constants.TIME_UNIT_KEY == "time_unit"