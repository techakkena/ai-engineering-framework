import pytest

from ai_observability.metrics.exceptions import (
    MetricsError,
)


def test_metrics_error() -> None:
    with pytest.raises(MetricsError):
        raise MetricsError()
