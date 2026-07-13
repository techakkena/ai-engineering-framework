"""Constants for the ai_memory.conversation module."""

from __future__ import annotations

from enum import Enum


class ConversationType(str, Enum):
    """Supported conversation memory types."""

    SESSION = "session"
    PERSISTENT = "persistent"


class ConversationState(str, Enum):
    """Conversation lifecycle states."""

    ACTIVE = "active"
    INACTIVE = "inactive"
    ARCHIVED = "archived"


class ConversationRole(str, Enum):
    """Supported conversation roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


DEFAULT_MAX_MESSAGES = 100
DEFAULT_CONVERSATION_NAME = "conversation"
