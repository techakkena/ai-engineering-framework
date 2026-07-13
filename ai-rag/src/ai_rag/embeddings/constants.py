"""Constants for embedding models."""

DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"

DEFAULT_EMBEDDING_DIMENSIONS = 1536

SUPPORTED_EMBEDDING_MODELS = (
    "text-embedding-3-small",
    "text-embedding-3-large",
    "text-embedding-ada-002",
)

MODEL_DIMENSIONS = {
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
    "text-embedding-ada-002": 1536,
}