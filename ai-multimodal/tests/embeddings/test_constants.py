"""
Unit tests for ai_multimodal.embeddings.constants.
"""

from __future__ import annotations

from ai_multimodal.embeddings import constants


def test_supported_tasks() -> None:
    """Supported tasks should contain all embedding tasks."""
    assert constants.TASK_CREATE in constants.SUPPORTED_TASKS
    assert constants.TASK_COMPARE in constants.SUPPORTED_TASKS
    assert constants.TASK_SEARCH in constants.SUPPORTED_TASKS
    assert constants.TASK_UPDATE in constants.SUPPORTED_TASKS
    assert constants.TASK_METADATA in constants.SUPPORTED_TASKS


def test_supported_embedding_types() -> None:
    """Embedding types should contain all supported modalities."""
    assert constants.EMBEDDING_TYPE_TEXT in constants.SUPPORTED_EMBEDDING_TYPES
    assert constants.EMBEDDING_TYPE_IMAGE in constants.SUPPORTED_EMBEDDING_TYPES
    assert constants.EMBEDDING_TYPE_AUDIO in constants.SUPPORTED_EMBEDDING_TYPES
    assert constants.EMBEDDING_TYPE_VIDEO in constants.SUPPORTED_EMBEDDING_TYPES
    assert (
        constants.EMBEDDING_TYPE_DOCUMENT
        in constants.SUPPORTED_EMBEDDING_TYPES
    )


def test_default_vector_dimensions() -> None:
    """Vector dimensions should be positive."""
    assert constants.DEFAULT_VECTOR_DIMENSIONS > 0
    assert (
        constants.DEFAULT_VECTOR_DIMENSIONS
        <= constants.MAX_VECTOR_DIMENSIONS
    )


def test_top_k_limits() -> None:
    """Top-k values should be valid."""
    assert constants.DEFAULT_TOP_K > 0
    assert constants.DEFAULT_TOP_K <= constants.MAX_TOP_K


def test_similarity_metrics() -> None:
    """Similarity metrics should contain expected values."""
    assert constants.SIMILARITY_COSINE in (
        constants.SUPPORTED_SIMILARITY_METRICS
    )
    assert constants.SIMILARITY_DOT_PRODUCT in (
        constants.SUPPORTED_SIMILARITY_METRICS
    )
    assert constants.SIMILARITY_EUCLIDEAN in (
        constants.SUPPORTED_SIMILARITY_METRICS
    )


def test_similarity_thresholds() -> None:
    """Similarity thresholds should be valid."""
    assert constants.MIN_SIMILARITY_THRESHOLD == 0.0
    assert constants.DEFAULT_SIMILARITY_THRESHOLD == 0.75
    assert constants.MAX_SIMILARITY_THRESHOLD == 1.0


def test_metadata_keys() -> None:
    """Metadata keys should match expected values."""
    assert constants.METADATA_PROVIDER == "provider"
    assert constants.METADATA_MODEL == "model"
    assert constants.METADATA_DIMENSIONS == "dimensions"
    assert constants.METADATA_METRIC == "similarity_metric"
    assert constants.METADATA_LATENCY == "latency_ms"