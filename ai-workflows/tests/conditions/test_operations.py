from ai_workflows.conditions.operations import (
    Condition,
)


def test_default_condition() -> None:
    condition = Condition()

    assert condition.name == "condition"
    assert "Default" in condition.description


def test_custom_condition() -> None:
    condition = Condition(
        name="authenticated",
        description="User authenticated",
    )

    assert condition.name == "authenticated"
    assert condition.description == "User authenticated"


def test_true_condition() -> None:
    condition = Condition()

    assert condition.evaluate(True)


def test_false_condition() -> None:
    condition = Condition()

    assert not condition.evaluate(False)


def test_non_empty_string() -> None:
    condition = Condition()

    assert condition.evaluate("hello")


def test_empty_string() -> None:
    condition = Condition()

    assert not condition.evaluate("")
