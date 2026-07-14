from ai_observability.latency.constants import (
    DEFAULT_LATENCY_UNIT,
)


def test_default_unit() -> None:
    assert DEFAULT_LATENCY_UNIT == "ms"
