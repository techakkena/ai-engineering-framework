from ai_workflows.pipeline.constants import (
    DEFAULT_PIPELINE_NAME,
)


def test_default_pipeline_name() -> None:
    assert DEFAULT_PIPELINE_NAME == "pipeline"
