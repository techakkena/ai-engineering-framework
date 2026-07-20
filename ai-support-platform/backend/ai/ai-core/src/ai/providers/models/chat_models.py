from __future__ import annotations

"""
AI Engineering Framework
Chat Models

Author : TECHAKKENA
"""

from enum import Enum


class ChatModels(str, Enum):
    """
    Supported chat models.
    """

    GPT5 = "gpt-5"

    GPT5_MINI = "gpt-5-mini"

    GPT5_NANO = "gpt-5-nano"

    GPT4_1 = "gpt-4.1"

    GPT4_1_MINI = "gpt-4.1-mini"

    GPT4O = "gpt-4o"

    GPT4O_MINI = "gpt-4o-mini"

    O1 = "o1"

    O3 = "o3"

    O4_MINI = "o4-mini"
