"""
AI Engineering Framework
AI Chat Types

Author : TECHAKKENA
"""

from enum import Enum
from typing import Any

from constants.ai_constants import ChatModels
from pydantic import BaseModel, Field


class ChatRole(str, Enum):
    """
    Supported chat roles.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class ChatMessage(BaseModel):
    """
    Represents a single chat message.
    """

    role: ChatRole
    content: str

    name: str | None = None

    metadata: dict[str, Any] = Field(
        default_factory=dict,
    )


class ChatResponse(BaseModel):
    """
    Represents a chat response.
    """

    content: str

    model: str

    finish_reason: str = "stop"

    usage: dict[str, int] = Field(
        default_factory=dict,
    )


class ChatOptions(BaseModel):
    """
    Chat request configuration.
    """

    model: str = ChatModels.GPT_5_5

    temperature: float = 0.2

    max_tokens: int = 4096

    stream: bool = False

    session_id: str | None = None
