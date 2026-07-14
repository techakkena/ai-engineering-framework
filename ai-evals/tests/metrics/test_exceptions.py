import pytest

from ai_evals.metrics.exceptions import (
    MetricError,
)


def test_metric_error() -> None:
    with pytest.raises(MetricError):
        raise MetricError()
