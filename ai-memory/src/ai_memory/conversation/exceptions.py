"""Exceptions for the ai_memory.conversation module."""

from __future__ import annotations


class ConversationError(Exception):
    """Base exception for conversation operations."""


class ConversationNotFoundError(ConversationError):
    """Raised when a conversation cannot be found."""


class ConversationValidationError(ConversationError):
    """Raised when conversation validation fails."""


class ConversationStateError(ConversationError):
    """Raised when an invalid conversation state is encountered."""
