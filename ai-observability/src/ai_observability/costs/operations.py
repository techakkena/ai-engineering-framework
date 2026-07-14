from __future__ import annotations

from dataclasses import dataclass

from .constants import DEFAULT_CURRENCY


@dataclass(slots=True)
class CostRecord:
    """Represents an AI cost record."""

    amount: float
    currency: str = DEFAULT_CURRENCY


class CostRegistry:
    """Registry for AI costs."""

    def __init__(self) -> None:
        self._records: list[CostRecord] = []

    def add(
        self,
        record: CostRecord,
    ) -> None:
        """Add a cost record."""
        self._records.append(record)

    @property
    def count(self) -> int:
        """Return number of records."""
        return len(self._records)

    @property
    def total_cost(self) -> float:
        """Return total cost."""
        return sum(record.amount for record in self._records)

    @property
    def average_cost(self) -> float:
        """Return average cost."""
        if not self._records:
            return 0.0

        return self.total_cost / self.count
