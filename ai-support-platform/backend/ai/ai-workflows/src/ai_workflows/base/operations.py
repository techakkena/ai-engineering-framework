from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowInput:
    """Workflow input."""

    data: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class WorkflowOutput:
    """Workflow output."""

    result: Any = None
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class WorkflowContext:
    """Workflow runtime context."""

    workflow_id: str | None = None
    variables: dict[str, Any] = field(default_factory=dict)


class BaseWorkflow(ABC):
    """Abstract base class for workflows."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return workflow name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Return workflow description."""

    @abstractmethod
    async def run(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        """Execute the workflow."""

    async def initialize(self) -> None:
        """Initialize workflow resources."""

    async def shutdown(self) -> None:
        """Release workflow resources."""

    async def before_run(
        self,
        workflow_input: WorkflowInput,
    ) -> None:
        """Hook executed before run."""

    async def after_run(
        self,
        workflow_output: WorkflowOutput,
    ) -> None:
        """Hook executed after run."""
