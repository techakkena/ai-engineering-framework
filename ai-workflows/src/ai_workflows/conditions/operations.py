from __future__ import annotations

from abc import ABC, abstractmethod

from .constants import (
    DEFAULT_CONDITION_DESCRIPTION,
    DEFAULT_CONDITION_NAME,
)


class BaseCondition(ABC):
    """Abstract workflow condition."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return condition name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Return condition description."""

    @abstractmethod
    def evaluate(self, value: object) -> bool:
        """Evaluate a condition."""


class Condition(BaseCondition):
    """Simple workflow condition."""

    def __init__(
        self,
        name: str = DEFAULT_CONDITION_NAME,
        description: str = DEFAULT_CONDITION_DESCRIPTION,
    ) -> None:
        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        """Return condition name."""
        return self._name

    @property
    def description(self) -> str:
        """Return condition description."""
        return self._description

    def evaluate(
        self,
        value: object,
    ) -> bool:
        """Return boolean representation."""
        return bool(value)
