"""
AI Engineering Framework
AI Chat Schemas

Author : TECHAKKENA
"""

from pydantic import BaseModel, Field

from .types import ChatOptions


class ChatRequest(BaseModel):
    """
    Chat request schema.
    """

    message: str = Field(
        ...,
        min_length=1,
        description="User message",
    )

    options: ChatOptions = Field(
        default_factory=ChatOptions,
    )


class ChatResponseSchema(BaseModel):
    """
    Chat response schema.
    """

    response: str

    model: str

    session_id: str | None = None

    finish_reason: str = "stop"


class HealthResponse(BaseModel):
    """
    Service health response.
    """

    status: str = "healthy"

    service: str = "ai-chat"

    version: str = "0.1.0"
