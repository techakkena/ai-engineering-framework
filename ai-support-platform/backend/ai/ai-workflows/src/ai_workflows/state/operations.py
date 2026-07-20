from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowState:
    """Represents workflow state."""

    name: str
    data: dict[str, Any] = field(default_factory=dict)


class WorkflowStateStore:
    """In-memory workflow state store."""

    def __init__(self) -> None:
        self._states: dict[str, WorkflowState] = {}

    def set(
        self,
        state: WorkflowState,
    ) -> None:
        """Store a workflow state."""
        self._states[state.name] = state

    def get(
        self,
        name: str,
    ) -> WorkflowState:
        """Retrieve a workflow state."""
        return self._states[name]

    def exists(
        self,
        name: str,
    ) -> bool:
        """Return whether a state exists."""
        return name in self._states

    def remove(
        self,
        name: str,
    ) -> None:
        """Remove a workflow state."""
        del self._states[name]

    def clear(self) -> None:
        """Remove all workflow states."""
        self._states.clear()

    @property
    def size(self) -> int:
        """Return number of stored states."""
        return len(self._states)
