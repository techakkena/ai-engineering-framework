from ai_observability.token_usage.constants import (
    DEFAULT_MODEL_NAME,
)


def test_default_model_name() -> None:
    assert DEFAULT_MODEL_NAME == "unknown"
