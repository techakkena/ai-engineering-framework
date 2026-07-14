from ai_tools.calendar.operations import (
    CalendarClient,
    CalendarEvent,
)


def test_add_event() -> None:
    client = CalendarClient()

    event = CalendarEvent(
        event_id="1",
        title="Team Meeting",
        start_time="2026-07-15T10:00:00",
        end_time="2026-07-15T11:00:00",
    )

    client.add_event(event)

    assert client.event_count == 1


def test_get_event() -> None:
    client = CalendarClient()

    event = CalendarEvent(
        event_id="1",
        title="Team Meeting",
        start_time="2026-07-15T10:00:00",
        end_time="2026-07-15T11:00:00",
    )

    client.add_event(event)

    result = client.get_event("1")

    assert result is event


def test_missing_event() -> None:
    client = CalendarClient()

    assert client.get_event("missing") is None


def test_list_events() -> None:
    client = CalendarClient()

    client.add_event(
        CalendarEvent(
            event_id="1",
            title="Meeting",
            start_time="2026-07-15T10:00:00",
            end_time="2026-07-15T11:00:00",
        )
    )

    events = client.list_events()

    assert len(events) == 1
    assert events[0].title == "Meeting"
