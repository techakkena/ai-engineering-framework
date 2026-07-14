from ai_observability.events.constants import (
    EventType,
)


def test_event_types() -> None:
    assert EventType.INFO.value == "info"
    assert EventType.ERROR.value == "error"


def test_event_type_count() -> None:
    assert len(EventType) == 3
