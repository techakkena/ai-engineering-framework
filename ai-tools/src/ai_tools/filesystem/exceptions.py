"""Filesystem exceptions."""

from ai_agents.tools.exceptions import ToolExecutionError


class FileSystemToolError(ToolExecutionError):
    """Raised when filesystem operations fail."""
