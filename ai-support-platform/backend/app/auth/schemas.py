from __future__ import annotations

"""Authentication schemas."""

from datetime import UTC, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class LoginRequest(BaseModel):
    """Login request schema."""

    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128,
    )


class TokenResponse(BaseModel):
    """JWT token response schema."""

    access_token: str
    token_type: str = "Bearer"
    expires_in: int


class RefreshTokenRequest(BaseModel):
    """Refresh token request schema."""

    refresh_token: str


class UserResponse(BaseModel):
    """Authenticated user response."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    
    id: UUID
    email: EmailStr
    username: str
    full_name: str
    is_active: bool
    is_superuser: bool
    created_at: datetime


class CurrentUserResponse(BaseModel):
    """Current user response."""

    user: UserResponse
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
    )