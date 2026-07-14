from ai_observability.exporters.constants import (
    DEFAULT_EXPORTER_NAME,
)


def test_default_exporter_name() -> None:
    assert DEFAULT_EXPORTER_NAME == "memory"
