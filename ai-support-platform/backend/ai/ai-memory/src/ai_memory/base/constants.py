from __future__ import annotations

from enum import Enum


class MemoryType(str, Enum):
    BUFFER = "buffer"
    CONVERSATION = "conversation"
    SUMMARY = "summary"
    ENTITY = "entity"
    VECTOR = "vector"


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class MemoryScope(str, Enum):
    SESSION = "session"
    USER = "user"
    GLOBAL = "global"


class MemoryFormat(str, Enum):
    TEXT = "text"
    JSON = "json"
