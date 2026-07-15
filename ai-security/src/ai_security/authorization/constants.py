"""
Constants for ai_security.authorization.
"""

from __future__ import annotations

from typing import Final

# ============================================================================
# Defaults
# ============================================================================

DEFAULT_AUTHORIZATION_PROVIDER: Final[str] = "rbac"

DEFAULT_ROLE: Final[str] = "user"

DEFAULT_POLICY: Final[str] = "default"

# ============================================================================
# Providers
# ============================================================================

RBAC: Final[str] = "rbac"

ABAC: Final[str] = "abac"

ACL: Final[str] = "acl"

OPA: Final[str] = "opa"

CASBIN: Final[str] = "casbin"

SUPPORTED_AUTHORIZATION_PROVIDERS: Final[
    frozenset[str]
] = frozenset(
    {
        RBAC,
        ABAC,
        ACL,
        OPA,
        CASBIN,
    }
)

# ============================================================================
# Configuration
# ============================================================================

DEFAULT_TIMEOUT: Final[int] = 30

DEFAULT_RETRIES: Final[int] = 3