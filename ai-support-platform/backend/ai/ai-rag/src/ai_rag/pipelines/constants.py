from __future__ import annotations

"""Constants for RAG pipelines."""

DEFAULT_PIPELINE = "retrieval"

SUPPORTED_PIPELINES = (
    "indexing",
    "retrieval",
    "ingestion",
)

DEFAULT_MAX_STEPS = 10

MIN_STEPS = 1

MAX_STEPS = 100
