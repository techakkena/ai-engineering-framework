from __future__ import annotations

"""
AI Engineering Framework
Moderation Models

Author : TECHAKKENA
"""

from enum import Enum


class ModerationModels(str, Enum):
    """
    Supported moderation models.
    """

    OMNI_MODERATION_LATEST = "omni-moderation-latest"

    TEXT_MODERATION_LATEST = "text-moderation-latest"
