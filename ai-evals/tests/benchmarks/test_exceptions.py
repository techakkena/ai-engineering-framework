import pytest

from ai_evals.benchmarks.exceptions import (
    BenchmarkError,
)


def test_benchmark_error() -> None:
    with pytest.raises(BenchmarkError):
        raise BenchmarkError()
