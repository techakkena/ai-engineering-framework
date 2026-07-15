"""
Tests for ai_security.utils.operations.
"""

import pytest

from ai_security.utils.operations import SecurityUtils


def test_mask_secret_default() -> None:
    """Mask a secret using the default visible characters."""
    secret = "abcdefghijklmnopqrstuvwxyz"

    masked = SecurityUtils.mask_secret(secret)

    assert masked.endswith("wxyz")
    assert len(masked) == len(secret)
    assert masked[:-4] == "*" * (len(secret) - 4)


def test_mask_secret_zero_visible() -> None:
    """Mask the entire secret."""
    secret = "password"

    masked = SecurityUtils.mask_secret(secret, visible=0)

    assert masked == "*" * len(secret)


def test_mask_secret_short_secret() -> None:
    """Short secrets should not be modified."""
    secret = "abc"

    assert SecurityUtils.mask_secret(secret) == "abc"


def test_mask_secret_invalid_visible() -> None:
    """Negative visible values should raise ValueError."""
    with pytest.raises(ValueError):
        SecurityUtils.mask_secret(
            "password",
            visible=-1,
        )


def test_constant_time_compare_equal() -> None:
    """Equal strings should compare successfully."""
    assert SecurityUtils.constant_time_compare(
        "secret",
        "secret",
    )


def test_constant_time_compare_not_equal() -> None:
    """Different strings should not compare successfully."""
    assert not SecurityUtils.constant_time_compare(
        "secret",
        "SECRET",
    )


def test_strong_password_valid() -> None:
    """A valid password should pass validation."""
    assert SecurityUtils.is_strong_password(
        "Strong@123"
    )


def test_strong_password_invalid() -> None:
    """A weak password should fail validation."""
    assert not SecurityUtils.is_strong_password(
        "password"
    )


def test_encode() -> None:
    """Encoding should return bytes."""
    value = SecurityUtils.encode("hello")

    assert isinstance(value, bytes)
    assert value == b"hello"


def test_decode() -> None:
    """Decoding should return a string."""
    value = SecurityUtils.decode(b"hello")

    assert isinstance(value, str)
    assert value == "hello"