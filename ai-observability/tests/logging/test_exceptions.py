import pytest

from ai_observability.logging.exceptions import (
    LoggingError,
)


def test_logging_error() -> None:
    with pytest.raises(LoggingError):
        raise LoggingError()
