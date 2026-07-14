from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .constants import DEFAULT_DATASET_NAME


@dataclass(slots=True)
class EvaluationCase:
    ...
    """Represents a single evaluation test case."""

    inputs: dict[str, Any]

    expected_output: Any


@dataclass(slots=True)
class Dataset:
    """Represents an evaluation dataset."""

    name: str = DEFAULT_DATASET_NAME

    test_cases: list[EvaluationCase] = field(
        default_factory=list,
    )

    def add_test_case(
        self,
        test_case: EvaluationCase,
    ) -> None:
        """Add a test case."""
        self.test_cases.append(test_case)


class DatasetRegistry:
    """Registry of evaluation datasets."""

    def __init__(self) -> None:
        self._datasets: dict[str, Dataset] = {}

    def register(
        self,
        dataset: Dataset,
    ) -> None:
        self._datasets[dataset.name] = dataset

    def get(
        self,
        name: str,
    ) -> Dataset | None:
        return self._datasets.get(name)

    @property
    def count(self) -> int:
        return len(self._datasets)
