from __future__ import annotations

"""Exceptions for workflow routing."""

from ai_workflows.base.exceptions import WorkflowError


class RouteAlreadyExistsError(WorkflowError):
    """Raised when a route already exists."""


class RouteNotFoundError(WorkflowError):
    """Raised when a route cannot be found."""
