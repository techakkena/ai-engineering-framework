"""Exceptions for the base prompt module."""


class PromptError(Exception):
    """Base exception for prompt operations."""


class InvalidPromptError(PromptError):
    """Raised when a prompt is invalid."""


class PromptNotFoundError(PromptError):
    """Raised when a prompt cannot be found."""
