from __future__ import annotations

"""Constants for retrievers."""

DEFAULT_RETRIEVER = "similarity"

DEFAULT_TOP_K = 5

SUPPORTED_RETRIEVERS = (
    "similarity",
    "mmr",
    "hybrid",
)

MIN_TOP_K = 1

MAX_TOP_K = 100
