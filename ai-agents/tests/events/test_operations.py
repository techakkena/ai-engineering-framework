from ai_agents.events.operations import (
    Event,
    EventDispatcher,
)


def test_event_creation() -> None:
    event = Event(
        event_type="test",
    )

    assert event.event_type == "test"
    assert event.payload == {}


def test_subscribe() -> None:
    dispatcher = EventDispatcher()

    dispatcher.subscribe(
        "test",
        lambda event: None,
    )

    assert dispatcher.handler_count("test") == 1


def test_publish() -> None:
    dispatcher = EventDispatcher()

    received: list[dict[str, int]] = []

    def handler(event: Event) -> None:
        received.append(event.payload)

    dispatcher.subscribe(
        "test",
        handler,
    )

    dispatcher.publish(
        Event(
            event_type="test",
            payload={"value": 10},
        )
    )

    assert received == [{"value": 10}]


def test_publish_without_handlers() -> None:
    dispatcher = EventDispatcher()

    dispatcher.publish(
        Event(
            event_type="missing",
        )
    )

    assert dispatcher.handler_count("missing") == 0


def test_clear() -> None:
    dispatcher = EventDispatcher()

    dispatcher.subscribe(
        "test",
        lambda event: None,
    )

    dispatcher.clear()

    assert dispatcher.handler_count("test") == 0
