from ai_evals.datasets.operations import (
    Dataset,
    DatasetRegistry,
    EvaluationCase,
)


def test_dataset_defaults() -> None:
    dataset = Dataset()

    assert dataset.name == "default"
    assert dataset.test_cases == []


def test_add_test_case() -> None:
    dataset = Dataset()

    dataset.add_test_case(
        EvaluationCase(
            inputs={
                "question": "2+2",
            },
            expected_output="4",
        )
    )

    assert len(dataset.test_cases) == 1


def test_dataset_registry() -> None:
    registry = DatasetRegistry()

    dataset = Dataset(
        name="math",
    )

    registry.register(dataset)

    assert registry.count == 1
    assert registry.get("math") is dataset


def test_missing_dataset() -> None:
    registry = DatasetRegistry()

    assert registry.get("missing") is None
