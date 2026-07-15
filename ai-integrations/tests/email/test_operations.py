"""
Tests for ai_integrations.email.operations.
"""

import pytest

from ai_integrations.email.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_PORT,
    DEFAULT_SMTP_HOST,
    DEFAULT_TIMEOUT,
)
from ai_integrations.email.exceptions import (
    EmailConfigurationError,
)
from ai_integrations.email.operations import (
    EmailAttachment,
    EmailClient,
    EmailMessage,
)


def test_attachment() -> None:
    """EmailAttachment should retain values."""
    attachment = EmailAttachment(
        filename="report.pdf",
        content_type="application/pdf",
        data=b"test",
    )

    assert attachment.filename == "report.pdf"
    assert attachment.content_type == "application/pdf"
    assert attachment.data == b"test"


def test_email_message() -> None:
    """EmailMessage should retain values."""
    attachment = EmailAttachment(
        filename="file.txt",
        content_type="text/plain",
        data=b"hello",
    )

    message = EmailMessage(
        sender="sender@example.com",
        recipients=("user@example.com",),
        subject="Test",
        body="Hello",
        attachments=(attachment,),
    )

    assert message.sender == "sender@example.com"
    assert len(message.attachments) == 1


def test_client_defaults() -> None:
    """Client should expose default configuration."""
    client = EmailClient(
        username="user",
        password="password",
    )

    health = client.health_check()

    assert health["provider"] == "email"
    assert health["host"] == DEFAULT_SMTP_HOST
    assert health["port"] == DEFAULT_PORT
    assert health["timeout"] == DEFAULT_TIMEOUT
    assert health["max_retries"] == DEFAULT_MAX_RETRIES
    assert health["configured"] is True


def test_invalid_username() -> None:
    """Empty username should fail."""
    with pytest.raises(EmailConfigurationError):
        EmailClient(
            username="",
            password="password",
        )


def test_invalid_password() -> None:
    """Empty password should fail."""
    with pytest.raises(EmailConfigurationError):
        EmailClient(
            username="user",
            password="",
        )


def test_send_email() -> None:
    """Sending an email should succeed."""
    client = EmailClient(
        username="user",
        password="password",
    )

    message = EmailMessage(
        sender="sender@example.com",
        recipients=("user@example.com",),
        subject="Hello",
        body="World",
    )

    assert client.send(message)


def test_send_without_recipients() -> None:
    """Sending without recipients should fail."""
    client = EmailClient(
        username="user",
        password="password",
    )

    message = EmailMessage(
        sender="sender@example.com",
        recipients=(),
        subject="Hello",
        body="World",
    )

    with pytest.raises(EmailConfigurationError):
        client.send(message)


def test_send_without_subject() -> None:
    """Sending without a subject should fail."""
    client = EmailClient(
        username="user",
        password="password",
    )

    message = EmailMessage(
        sender="sender@example.com",
        recipients=("user@example.com",),
        subject="",
        body="World",
    )

    with pytest.raises(EmailConfigurationError):
        client.send(message)


def test_custom_configuration() -> None:
    """Custom configuration should be retained."""
    client = EmailClient(
        username="user",
        password="password",
        host="smtp.example.com",
        port=465,
        timeout=120.0,
        max_retries=5,
    )

    health = client.health_check()

    assert health["host"] == "smtp.example.com"
    assert health["port"] == 465
    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5