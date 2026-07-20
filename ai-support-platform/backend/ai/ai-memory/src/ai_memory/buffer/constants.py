from __future__ import annotations

"""Constants for the ai_memory.buffer module."""

from __future__ import annotations

from enum import Enum


class BufferType(str, Enum):
    """Supported buffer implementations."""

    CONVERSATION = "conversation"
    WINDOW = "window"
    TOKEN = "token"


class BufferStrategy(str, Enum):
    """Supported buffer strategies."""

    FIFO = "fifo"
    LIFO = "lifo"
    SLIDING = "sliding"


DEFAULT_BUFFER_SIZE = 100
DEFAULT_WINDOW_SIZE = 20
DEFAULT_TOKEN_LIMIT = 4096
