"""Operations for indexing."""

from .constants import (
    DEFAULT_BATCH_SIZE,
    DEFAULT_INDEX_NAME,
    MAX_BATCH_SIZE,
    MIN_BATCH_SIZE,
)


def default_index_name() -> str:
    """Return the default index name."""

    return DEFAULT_INDEX_NAME


def default_batch_size() -> int:
    """Return the default batch size."""

    return DEFAULT_BATCH_SIZE


def validate_index_name(name: str) -> bool:
    """Validate an index name."""

    return bool(name.strip())


def validate_batch_size(batch_size: int) -> bool:
    """Validate a batch size."""

    return (
        MIN_BATCH_SIZE
        <= batch_size
        <= MAX_BATCH_SIZE
    )