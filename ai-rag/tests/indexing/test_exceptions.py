from ai_rag.indexing.exceptions import (
    IndexingError,
    InvalidBatchSizeError,
    InvalidIndexNameError,
)


def test_indexing_error():
    assert issubclass(
        IndexingError,
        Exception,
    )


def test_invalid_index_name_error():
    assert issubclass(
        InvalidIndexNameError,
        IndexingError,
    )


def test_invalid_batch_size_error():
    assert issubclass(
        InvalidBatchSizeError,
        IndexingError,
    )