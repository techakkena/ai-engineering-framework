"""
Tests for ai_integrations.base.constants.
"""

from ai_integrations.base.constants import (
    DEFAULT_BATCH_SIZE,
    DEFAULT_EMBEDDING_DIMENSIONS,
    DEFAULT_ENCODING,
    DEFAULT_FREQUENCY_PENALTY,
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_TOKENS,
    DEFAULT_PRESENCE_PENALTY,
    DEFAULT_SEED,
    DEFAULT_STREAM,
    DEFAULT_TEMPERATURE,
    DEFAULT_TIMEOUT,
    DEFAULT_TOP_P,
    DEFAULT_USER_AGENT,
    MAX_TEMPERATURE,
    MAX_TOP_P,
    MIN_TEMPERATURE,
    MIN_TOP_P,
    SUPPORTED_FINISH_REASONS,
    SUPPORTED_MESSAGE_ROLES,
)


def test_default_timeout() -> None:
    """Test default timeout."""
    assert DEFAULT_TIMEOUT == 60.0


def test_default_max_retries() -> None:
    """Test default retry count."""
    assert DEFAULT_MAX_RETRIES == 3


def test_default_max_tokens() -> None:
    """Test default max tokens."""
    assert DEFAULT_MAX_TOKENS == 4096


def test_default_temperature() -> None:
    """Test default temperature."""
    assert DEFAULT_TEMPERATURE == 0.7


def test_default_top_p() -> None:
    """Test default top_p."""
    assert DEFAULT_TOP_P == 1.0


def test_default_penalties() -> None:
    """Test default penalties."""
    assert DEFAULT_FREQUENCY_PENALTY == 0.0
    assert DEFAULT_PRESENCE_PENALTY == 0.0


def test_temperature_limits() -> None:
    """Test temperature limits."""
    assert MIN_TEMPERATURE == 0.0
    assert MAX_TEMPERATURE == 2.0


def test_top_p_limits() -> None:
    """Test top_p limits."""
    assert MIN_TOP_P == 0.0
    assert MAX_TOP_P == 1.0


def test_default_embedding_dimensions() -> None:
    """Test embedding dimensions."""
    assert DEFAULT_EMBEDDING_DIMENSIONS == 1536


def test_default_batch_size() -> None:
    """Test batch size."""
    assert DEFAULT_BATCH_SIZE == 100


def test_default_encoding() -> None:
    """Test encoding."""
    assert DEFAULT_ENCODING == "utf-8"


def test_default_stream() -> None:
    """Test stream flag."""
    assert DEFAULT_STREAM is False


def test_default_seed() -> None:
    """Test default seed."""
    assert DEFAULT_SEED is None


def test_default_user_agent() -> None:
    """Test user agent."""
    assert DEFAULT_USER_AGENT.startswith(
        "AI-Engineering-Framework"
    )


def test_supported_roles() -> None:
    """Test supported roles."""
    assert "system" in SUPPORTED_MESSAGE_ROLES
    assert "user" in SUPPORTED_MESSAGE_ROLES
    assert "assistant" in SUPPORTED_MESSAGE_ROLES
    assert "tool" in SUPPORTED_MESSAGE_ROLES


def test_supported_finish_reasons() -> None:
    """Test supported finish reasons."""
    assert "stop" in SUPPORTED_FINISH_REASONS
    assert "length" in SUPPORTED_FINISH_REASONS