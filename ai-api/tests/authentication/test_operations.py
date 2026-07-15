"""
Unit tests for ai_api.authentication.operations.
"""

from __future__ import annotations

import pytest

from ai_api.authentication.exceptions import (
    InvalidTokenError,
    MissingAuthorizationHeaderError,
    UnsupportedAuthenticationSchemeError,
)
from ai_api.authentication.operations import (
    build_authorization_header,
    extract_bearer_token,
    is_bearer_token,
    is_supported_auth_scheme,
    normalize_auth_scheme,
    split_authorization_header,
    validate_auth_scheme,
    validate_token,
)


# ============================================================================
# normalize_auth_scheme
# ============================================================================


@pytest.mark.parametrize(
    ("scheme", "expected"),
    [
        ("Bearer", "bearer"),
        (" BASIC ", "basic"),
        ("OAuth2", "oauth2"),
        ("JWT", "jwt"),
        ("Session", "session"),
    ],
)
def test_normalize_auth_scheme(
    scheme: str,
    expected: str,
) -> None:
    """Test authentication scheme normalization."""
    assert normalize_auth_scheme(scheme) == expected


# ============================================================================
# validate_auth_scheme
# ============================================================================


@pytest.mark.parametrize(
    "scheme",
    [
        "bearer",
        "basic",
        "apikey",
        "oauth2",
        "jwt",
        "session",
    ],
)
def test_validate_auth_scheme(
    scheme: str,
) -> None:
    """Test supported authentication schemes."""
    assert validate_auth_scheme(scheme) == scheme


@pytest.mark.parametrize(
    "scheme",
    [
        "",
        "oauth1",
        "ntlm",
        "kerberos",
        "custom",
    ],
)
def test_validate_auth_scheme_invalid(
    scheme: str,
) -> None:
    """Unsupported schemes should raise."""
    with pytest.raises(
        UnsupportedAuthenticationSchemeError,
    ):
        validate_auth_scheme(scheme)


# ============================================================================
# is_bearer_token
# ============================================================================


@pytest.mark.parametrize(
    ("authorization", "expected"),
    [
        ("Bearer abc123456", True),
        ("Bearer token", True),
        ("Basic abc123", False),
        ("", False),
    ],
)
def test_is_bearer_token(
    authorization: str,
    expected: bool,
) -> None:
    """Test Bearer token detection."""
    assert is_bearer_token(authorization) is expected


# ============================================================================
# extract_bearer_token
# ============================================================================


def test_extract_bearer_token() -> None:
    """Test Bearer token extraction."""
    token = extract_bearer_token(
        "Bearer abc123456"
    )

    assert token == "abc123456"


@pytest.mark.parametrize(
    "authorization",
    [
        "",
        " ",
    ],
)
def test_extract_bearer_token_missing_header(
    authorization: str,
) -> None:
    """Missing Authorization header should raise."""
    with pytest.raises(
        MissingAuthorizationHeaderError,
    ):
        extract_bearer_token(authorization)


@pytest.mark.parametrize(
    "authorization",
    [
        "Basic abc123",
        "Bearer",
        "Bearer ",
    ],
)
def test_extract_bearer_token_invalid(
    authorization: str,
) -> None:
    """Invalid Bearer token should raise."""
    with pytest.raises(
        InvalidTokenError,
    ):
        extract_bearer_token(authorization)


# ============================================================================
# validate_token
# ============================================================================


@pytest.mark.parametrize(
    "token",
    [
        "abcdefgh",
        "abcdefghijklmnop",
        "jwt-token-123",
    ],
)
def test_validate_token(
    token: str,
) -> None:
    """Test valid tokens."""
    assert validate_token(token) == token


@pytest.mark.parametrize(
    "token",
    [
        "",
        " ",
        "abc",
        "1234567",
    ],
)
def test_validate_token_invalid(
    token: str,
) -> None:
    """Invalid tokens should raise."""
    with pytest.raises(
        InvalidTokenError,
    ):
        validate_token(token)


# ============================================================================
# build_authorization_header
# ============================================================================


def test_build_authorization_header() -> None:
    """Test Authorization header generation."""
    header = build_authorization_header(
        "abcdefgh"
    )

    assert header == "Bearer abcdefgh"


# ============================================================================
# split_authorization_header
# ============================================================================


def test_split_authorization_header() -> None:
    """Test Authorization header splitting."""
    scheme, credentials = split_authorization_header(
        "Bearer abcdefgh"
    )

    assert scheme == "Bearer"
    assert credentials == "abcdefgh"


@pytest.mark.parametrize(
    "authorization",
    [
        "",
        " ",
    ],
)
def test_split_authorization_header_missing(
    authorization: str,
) -> None:
    """Missing Authorization header should raise."""
    with pytest.raises(
        MissingAuthorizationHeaderError,
    ):
        split_authorization_header(
            authorization,
        )


@pytest.mark.parametrize(
    "authorization",
    [
        "Bearer",
        "InvalidHeader",
    ],
)
def test_split_authorization_header_invalid(
    authorization: str,
) -> None:
    """Invalid Authorization header should raise."""
    with pytest.raises(
        InvalidTokenError,
    ):
        split_authorization_header(
            authorization,
        )


# ============================================================================
# is_supported_auth_scheme
# ============================================================================


@pytest.mark.parametrize(
    ("scheme", "expected"),
    [
        ("bearer", True),
        ("basic", True),
        ("apikey", True),
        ("oauth2", True),
        ("jwt", True),
        ("session", True),
        ("oauth1", False),
        ("kerberos", False),
        ("ntlm", False),
    ],
)
def test_is_supported_auth_scheme(
    scheme: str,
    expected: bool,
) -> None:
    """Test supported authentication scheme detection."""
    assert (
        is_supported_auth_scheme(scheme)
        is expected
    )