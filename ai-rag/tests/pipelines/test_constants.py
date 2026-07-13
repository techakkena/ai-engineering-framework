from ai_rag.pipelines.constants import (
    DEFAULT_MAX_STEPS,
    DEFAULT_PIPELINE,
    MAX_STEPS,
    MIN_STEPS,
    SUPPORTED_PIPELINES,
)


def test_default_pipeline():
    assert DEFAULT_PIPELINE == "retrieval"


def test_default_max_steps():
    assert DEFAULT_MAX_STEPS == 10


def test_supported_pipelines():
    assert "retrieval" in SUPPORTED_PIPELINES
    assert "indexing" in SUPPORTED_PIPELINES
    assert "ingestion" in SUPPORTED_PIPELINES


def test_step_limits():
    assert MIN_STEPS < MAX_STEPS