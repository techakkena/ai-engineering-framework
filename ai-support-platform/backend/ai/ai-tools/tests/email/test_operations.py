from __future__ import annotations

from ai_tools.email.operations import (
    EmailClient,
    EmailMessage,
)


def test_send_message() -> None:
    client = EmailClient()

    message = EmailMessage(
        to="user@example.com",
        body="Hello!",
    )

    client.send(message)

    assert client.message_count == 1


def test_list_messages() -> None:
    client = EmailClient()

    message = EmailMessage(
        to="user@example.com",
        body="Hello!",
        subject="Greeting",
    )

    client.send(message)

    messages = client.list_messages()

    assert len(messages) == 1
    assert messages[0].subject == "Greeting"


def test_default_subject() -> None:
    message = EmailMessage(
        to="user@example.com",
        body="Hello!",
    )

    assert message.subject == "No Subject"
