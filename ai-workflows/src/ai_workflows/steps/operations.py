from __future__ import annotations

from abc import ABC, abstractmethod

from ai_workflows.base.operations import (
    WorkflowInput,
    WorkflowOutput,
)

from .constants import (
    DEFAULT_STEP_DESCRIPTION,
    DEFAULT_STEP_NAME,
)


class BaseStep(ABC):
    """Abstract workflow step."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return step name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Return step description."""

    @abstractmethod
    async def execute(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        """Execute workflow step."""


class Step(BaseStep):
    """Default workflow step."""

    def __init__(
        self,
        name: str = DEFAULT_STEP_NAME,
        description: str = DEFAULT_STEP_DESCRIPTION,
    ) -> None:
        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        """Return step name."""
        return self._name

    @property
    def description(self) -> str:
        """Return step description."""
        return self._description

    async def execute(
        self,
        workflow_input: WorkflowInput,
    ) -> WorkflowOutput:
        """Execute the workflow step."""

        return WorkflowOutput(
            result=workflow_input.data,
        )
