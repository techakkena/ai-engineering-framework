import pytest

from ai_observability.tracing.exceptions import (
    TracingError,
)


def test_tracing_error() -> None:
    with pytest.raises(TracingError):
        raise TracingError()
