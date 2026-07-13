from ai_rag.pipelines.operations import (
    default_max_steps,
    default_pipeline,
    supported_pipeline,
    validate_pipeline_steps,
)


def test_default_pipeline():
    assert default_pipeline() == "retrieval"


def test_default_max_steps():
    assert default_max_steps() == 10


def test_supported_pipeline():
    assert supported_pipeline("retrieval")


def test_unsupported_pipeline():
    assert not supported_pipeline("unknown")


def test_valid_pipeline_steps():
    assert validate_pipeline_steps(5)


def test_invalid_pipeline_steps_low():
    assert not validate_pipeline_steps(0)


def test_invalid_pipeline_steps_high():
    assert not validate_pipeline_steps(1000)