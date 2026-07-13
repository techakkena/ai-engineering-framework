from ai_rag.pipelines.exceptions import (
    InvalidPipelineError,
    InvalidPipelineStepError,
    PipelineError,
)


def test_pipeline_error():
    assert issubclass(
        PipelineError,
        Exception,
    )


def test_invalid_pipeline_error():
    assert issubclass(
        InvalidPipelineError,
        PipelineError,
    )


def test_invalid_pipeline_step_error():
    assert issubclass(
        InvalidPipelineStepError,
        PipelineError,
    )