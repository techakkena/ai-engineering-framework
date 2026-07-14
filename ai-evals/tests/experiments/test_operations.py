import pytest

from ai_evals.experiments.operations import (
    Experiment,
    ExperimentRegistry,
)


def test_default_experiment() -> None:
    experiment = Experiment()

    assert experiment.name == "default"
    assert experiment.scores == {}


def test_record_score() -> None:
    experiment = Experiment()

    experiment.record_score(
        "accuracy",
        0.95,
    )

    assert experiment.scores["accuracy"] == 0.95


def test_average_score() -> None:
    experiment = Experiment()

    experiment.record_score(
        "accuracy",
        0.90,
    )

    experiment.record_score(
        "relevance",
        0.80,
    )

    assert experiment.average_score == pytest.approx(
        0.85,
    )


def test_registry() -> None:
    registry = ExperimentRegistry()

    experiment = Experiment(
        name="gpt5",
    )

    registry.register(
        experiment,
    )

    assert registry.count == 1

    assert registry.get("gpt5") is experiment
