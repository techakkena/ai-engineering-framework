"""Constants for the ai_testing.performance module."""

from __future__ import annotations

from typing import Final

DEFAULT_BENCHMARK_NAME: Final[str] = "benchmark"

DEFAULT_ITERATIONS: Final[int] = 1
DEFAULT_WARMUP_ITERATIONS: Final[int] = 0

MIN_ITERATIONS: Final[int] = 1
MAX_ITERATIONS: Final[int] = 1_000_000

DEFAULT_TIME_UNIT: Final[str] = "seconds"

SUPPORTED_TIME_UNITS: Final[frozenset[str]] = frozenset(
    {
        "seconds",
        "milliseconds",
        "microseconds",
        "nanoseconds",
    }
)

NAME_KEY: Final[str] = "name"
ITERATIONS_KEY: Final[str] = "iterations"
DURATION_KEY: Final[str] = "duration"
TIME_UNIT_KEY: Final[str] = "time_unit"

__all__ = [
    "DEFAULT_BENCHMARK_NAME",
    "DEFAULT_ITERATIONS",
    "DEFAULT_TIME_UNIT",
    "DEFAULT_WARMUP_ITERATIONS",
    "DURATION_KEY",
    "ITERATIONS_KEY",
    "MAX_ITERATIONS",
    "MIN_ITERATIONS",
    "NAME_KEY",
    "SUPPORTED_TIME_UNITS",
    "TIME_UNIT_KEY",
]