"""Operations for the ai_testing.performance module."""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter
from typing import Any, Callable

from ai_testing.performance.constants import (
    DEFAULT_ITERATIONS,
    DEFAULT_TIME_UNIT,
    MAX_ITERATIONS,
    MIN_ITERATIONS,
    SUPPORTED_TIME_UNITS,
)
from ai_testing.performance.exceptions import (
    InvalidIterationCountError,
    UnsupportedTimeUnitError,
)


@dataclass(slots=True, frozen=True)
class PerformanceResult:
    """Represents a benchmark result."""

    name: str
    iterations: int
    duration: float
    time_unit: str = DEFAULT_TIME_UNIT


class PerformanceRunner:
    """Runs simple performance benchmarks."""

    def measure(
        self,
        *,
        name: str,
        operation: Callable[[], Any],
        iterations: int = DEFAULT_ITERATIONS,
        time_unit: str = DEFAULT_TIME_UNIT,
    ) -> PerformanceResult:
        """Measure execution time."""

        if not (MIN_ITERATIONS <= iterations <= MAX_ITERATIONS):
            raise InvalidIterationCountError(
                "Iteration count is outside the allowed range."
            )

        if time_unit not in SUPPORTED_TIME_UNITS:
            raise UnsupportedTimeUnitError(
                f"Unsupported time unit: {time_unit!r}."
            )

        start = perf_counter()

        for _ in range(iterations):
            operation()

        duration = perf_counter() - start

        if time_unit == "milliseconds":
            duration *= 1_000
        elif time_unit == "microseconds":
            duration *= 1_000_000
        elif time_unit == "nanoseconds":
            duration *= 1_000_000_000

        return PerformanceResult(
            name=name.strip(),
            iterations=iterations,
            duration=duration,
            time_unit=time_unit,
        )


def measure_performance(
    *,
    name: str,
    operation: Callable[[], Any],
    iterations: int = DEFAULT_ITERATIONS,
    time_unit: str = DEFAULT_TIME_UNIT,
) -> PerformanceResult:
    """Measure the execution time of an operation."""

    return PerformanceRunner().measure(
        name=name,
        operation=operation,
        iterations=iterations,
        time_unit=time_unit,
    )


__all__ = [
    "PerformanceResult",
    "PerformanceRunner",
    "measure_performance",
]