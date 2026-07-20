from __future__ import annotations

from enum import Enum


class ChatModels(str, Enum):
    """
    Supported chat models.
    """

    GPT5 = "gpt-5"
    GPT5_MINI = "gpt-5-mini"
    GPT5_NANO = "gpt-5-nano"

    CLAUDE_SONNET = "claude-sonnet-4"
    CLAUDE_OPUS = "claude-opus-4"

    GEMINI_2_5_PRO = "gemini-2.5-pro"

    LLAMA3 = "llama3"


class EmbeddingModels(str, Enum):
    """
    Supported embedding models.
    """

    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"
    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"
