"""
Tests for ai_integrations.slack.operations.
"""

import pytest

from ai_integrations.slack.constants import (
    DEFAULT_API_BASE,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
)
from ai_integrations.slack.exceptions import (
    SlackConfigurationError,
)
from ai_integrations.slack.operations import (
    SlackChannel,
    SlackClient,
    SlackMessage,
)


def test_channel() -> None:
    """SlackChannel should retain values."""
    channel = SlackChannel(
        id="C123456",
        name="general",
    )

    assert channel.id == "C123456"
    assert channel.name == "general"


def test_message() -> None:
    """SlackMessage should retain values."""
    channel = SlackChannel(
        id="C123456",
        name="general",
    )

    message = SlackMessage(
        channel=channel,
        text="Hello Slack!",
    )

    assert message.channel == channel
    assert message.text == "Hello Slack!"


def test_client_defaults() -> None:
    """Client should expose default configuration."""
    client = SlackClient(
        token="test-token",
    )

    health = client.health_check()

    assert health["provider"] == "slack"
    assert health["api_base"] == DEFAULT_API_BASE
    assert health["timeout"] == DEFAULT_TIMEOUT
    assert health["max_retries"] == DEFAULT_MAX_RETRIES
    assert health["configured"] is True


def test_invalid_token() -> None:
    """Empty token should fail."""
    with pytest.raises(
        SlackConfigurationError,
    ):
        SlackClient(token="")


def test_send_message() -> None:
    """Message sending should succeed."""
    client = SlackClient(
        token="token",
    )

    channel = SlackChannel(
        id="C123456",
        name="general",
    )

    message = SlackMessage(
        channel=channel,
        text="Hello",
    )

    assert client.send_message(message)


def test_send_empty_message() -> None:
    """Empty message should fail."""
    client = SlackClient(
        token="token",
    )

    channel = SlackChannel(
        id="C123456",
        name="general",
    )

    message = SlackMessage(
        channel=channel,
        text="",
    )

    with pytest.raises(
        SlackConfigurationError,
    ):
        client.send_message(message)


def test_custom_configuration() -> None:
    """Custom configuration should be retained."""
    client = SlackClient(
        token="token",
        api_base="https://example.test/api",
        timeout=120.0,
        max_retries=5,
    )

    health = client.health_check()

    assert health["api_base"] == "https://example.test/api"
    assert health["timeout"] == 120.0
    assert health["max_retries"] == 5