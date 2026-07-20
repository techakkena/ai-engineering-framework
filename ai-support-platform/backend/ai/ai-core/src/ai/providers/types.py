from __future__ import annotations

"""
AI Engineering Framework
Provider Types

Author : TECHAKKENA
"""

from pydantic import BaseModel, Field


class ProviderConfig(BaseModel):
    """
    Provider configuration.
    """

    api_key: str | None = None

    model: str

    temperature: float = 0.2

    max_tokens: int = 4096

    timeout: int = 60

    stream: bool = False


class ProviderMessage(BaseModel):
    """
    Provider message.
    """

    role: str

    content: str


class ProviderUsage(BaseModel):
    """
    Token usage information.
    """

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0


class ProviderResponse(BaseModel):
    """
    Provider response.
    """

    content: str

    model: str

    finish_reason: str = "stop"

    usage: ProviderUsage = Field(
        default_factory=ProviderUsage,
    )
