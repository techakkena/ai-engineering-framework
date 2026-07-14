from ai_evals.benchmarks.constants import (
    DEFAULT_BENCHMARK_NAME,
)


def test_default_benchmark_name() -> None:
    assert DEFAULT_BENCHMARK_NAME == "default"
