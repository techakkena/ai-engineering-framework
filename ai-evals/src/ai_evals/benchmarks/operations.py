from __future__ import annotations

from dataclasses import dataclass

from ai_evals.datasets.operations import Dataset
from ai_evals.evaluators.operations import Evaluator

from .constants import DEFAULT_BENCHMARK_NAME


@dataclass(slots=True)
class Benchmark:
    """Represents a benchmark."""

    name: str = DEFAULT_BENCHMARK_NAME

    dataset: Dataset | None = None

    evaluator: Evaluator | None = None


class BenchmarkRunner:
    """Runs benchmarks."""

    def run(
        self,
        benchmark: Benchmark,
    ) -> int:
        """Run a benchmark.

        Returns the number of evaluation cases processed.
        """
        if benchmark.dataset is None:
            return 0

        return len(benchmark.dataset.test_cases)


class BenchmarkRegistry:
    """Registry of benchmarks."""

    def __init__(self) -> None:
        self._benchmarks: dict[str, Benchmark] = {}

    def register(
        self,
        benchmark: Benchmark,
    ) -> None:
        """Register a benchmark."""
        self._benchmarks[benchmark.name] = benchmark

    def get(
        self,
        name: str,
    ) -> Benchmark | None:
        """Return a benchmark."""
        return self._benchmarks.get(name)

    @property
    def count(self) -> int:
        """Return number of benchmarks."""
        return len(self._benchmarks)
