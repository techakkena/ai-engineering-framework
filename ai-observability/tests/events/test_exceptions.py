import pytest

from ai_observability.events.exceptions import (
    EventError,
)


def test_event_error() -> None:
    with pytest.raises(EventError):
        raise EventError()
