"""Constants for rerankers."""

DEFAULT_RERANKER = "cross-encoder"

DEFAULT_TOP_K = 10

SUPPORTED_RERANKERS = (
    "cross-encoder",
    "cohere",
    "jina",
    "voyage",
    "none",
)

MIN_TOP_K = 1

MAX_TOP_K = 100