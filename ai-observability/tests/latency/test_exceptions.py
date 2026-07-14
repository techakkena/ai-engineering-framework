import pytest

from ai_observability.latency.exceptions import (
    LatencyError,
)


def test_latency_error() -> None:
    with pytest.raises(
        LatencyError,
    ):
        raise LatencyError()
