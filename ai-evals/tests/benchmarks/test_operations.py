from ai_evals.benchmarks.operations import (
    Benchmark,
    BenchmarkRegistry,
    BenchmarkRunner,
)
from ai_evals.datasets.operations import (
    Dataset,
    EvaluationCase,
)
from ai_evals.evaluators.operations import (
    Evaluator,
)


def test_benchmark_defaults() -> None:
    benchmark = Benchmark()

    assert benchmark.name == "default"
    assert benchmark.dataset is None
    assert benchmark.evaluator is None


def test_runner_without_dataset() -> None:
    runner = BenchmarkRunner()

    assert runner.run(Benchmark()) == 0


def test_runner_with_dataset() -> None:
    dataset = Dataset()

    dataset.add_test_case(
        EvaluationCase(
            inputs={"question": "2+2"},
            expected_output="4",
        )
    )

    benchmark = Benchmark(
        dataset=dataset,
        evaluator=Evaluator(),
    )

    runner = BenchmarkRunner()

    assert runner.run(benchmark) == 1


def test_registry() -> None:
    registry = BenchmarkRegistry()

    benchmark = Benchmark(name="rag")

    registry.register(benchmark)

    assert registry.count == 1
    assert registry.get("rag") is benchmark
