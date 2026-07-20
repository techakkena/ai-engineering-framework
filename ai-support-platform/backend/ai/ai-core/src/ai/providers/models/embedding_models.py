from __future__ import annotations

"""
AI Engineering Framework
Embedding Models

Author : TECHAKKENA
"""

from enum import Enum


class EmbeddingModels(str, Enum):
    """
    Supported embedding models.
    """

    TEXT_EMBEDDING_3_SMALL = "text-embedding-3-small"

    TEXT_EMBEDDING_3_LARGE = "text-embedding-3-large"

    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"
