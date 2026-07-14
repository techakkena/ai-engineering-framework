import pytest

from ai_observability.exporters.exceptions import (
    ExporterError,
)


def test_exporter_error() -> None:
    with pytest.raises(ExporterError):
        raise ExporterError()
