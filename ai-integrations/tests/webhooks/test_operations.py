"""
Tests for ai_integrations.webhooks.operations.
"""

import pytest

from ai_integrations.webhooks.constants import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from ai_integrations.webhooks.exceptions import (
    WebhookConfigurationError,
)
from ai_integrations.webhooks.operations import (
    WebhookClient,
    WebhookEvent,
    WebhookRequest,
)


def test_webhook_event() -> None:
    """WebhookEvent should retain values."""
    event = WebhookEvent(
        name="push",
        payload={"ref": "main"},
    )

    assert event.name == "push"
    assert event.payload["ref"] == "main"


def test_webhook_request() -> None:
    """WebhookRequest should retain values."""
    request = WebhookRequest(
        url="https://example.com/webhook",
        method="POST",
        payload={"status": "ok"},
    )

    assert request.url == "https://example.com/webhook"
    assert request.method == "POST"
    assert request.payload["status"] == "ok"


def test_client_defaults() -> None:
    """Client should expose default configuration."""
    client = WebhookClient()

    health = client.health_check()

    assert health["provider"] == "webhooks"
    assert health["configured"] is True
    assert health["timeout"] == DEFAULT_TIMEOUT
    assert health["max_retries"] == DEFAULT_MAX_RETRIES


def test_send_webhook() -> None:
    """Sending a webhook should succeed."""
    client = WebhookClient()

    request = WebhookRequest(
        url="https://example.com/webhook",
        method="POST",
        payload={"hello": "world"},
    )

    assert client.send(request)


def test_empty_url() -> None:
    """Empty webhook URL should fail."""
    client = WebhookClient()

    request = WebhookRequest(
        url="",
        method="POST",
        payload={},
    )

    with pytest.raises(
        WebhookConfigurationError,
    ):
        client.send(request)


def test_verify_signature() -> None:
    """Signature verification should succeed."""
    client = WebhookClient()

    assert client.verify_signature(
        payload=b'{"hello":"world"}',
        signature="signature",
        secret="secret",
    )


def test_verify_signature_empty_secret() -> None:
    """Empty secret should fail."""
    client = WebhookClient()

    with pytest.raises(
        WebhookConfigurationError,
    ):
        client.verify_signature(
            payload=b"{}",
            signature="signature",
            secret="",
        )


def test_custom_configuration() -> None:
    """Custom configuration should be retained."""
    client = WebhookClient(
        timeout=120.0,
        max_retries=5,
    )

    health = client.health_check()

    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5