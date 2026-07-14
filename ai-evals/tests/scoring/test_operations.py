from ai_evals.scoring.operations import (
    Score,
    ScoreRegistry,
)

from math import isclose


def test_default_score() -> None:
    score = Score()

    assert score.name == "overall"
    assert score.value == 0.0


def test_register_score() -> None:
    registry = ScoreRegistry()

    score = Score(
        name="accuracy",
        value=0.95,
    )

    registry.register(score)

    assert registry.count == 1
    assert registry.get("accuracy") is score


def test_average_score() -> None:
    registry = ScoreRegistry()

    registry.register(
        Score(
            name="accuracy",
            value=0.90,
        )
    )

    registry.register(
        Score(
            name="relevance",
            value=0.80,
        )
    )

    assert isclose(
        registry.average_score,
        0.85,
    )


def test_empty_registry() -> None:
    registry = ScoreRegistry()

    assert registry.count == 0
    assert registry.average_score == 0.0
