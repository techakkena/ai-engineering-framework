from ai_observability.events.constants import (
    EventType,
)
from ai_observability.events.operations import (
    Event,
    EventBus,
)


def test_subscribe() -> None:
    bus = EventBus()

    received: list[Event] = []

    bus.subscribe(received.append)

    assert bus.subscriber_count == 1


def test_publish() -> None:
    bus = EventBus()

    received: list[Event] = []

    bus.subscribe(received.append)

    bus.publish(
        Event(
            name="workflow_started",
            event_type=EventType.INFO,
        )
    )

    assert len(received) == 1
    assert received[0].name == "workflow_started"
