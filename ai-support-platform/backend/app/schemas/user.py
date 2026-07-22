"""User schemas."""

from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """Base user schema."""

    email: EmailStr
    username: str = Field(
        min_length=3,
        max_length=100,
    )
    full_name: str = Field(
        min_length=1,
        max_length=255,
    )
    is_active: bool = True


class UserCreate(UserBase):
    """Schema for creating a user."""

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class UserUpdate(BaseModel):
    """Schema for updating a user."""

    email: EmailStr | None = None
    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
    )
    full_name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )
    password: str | None = Field(
        default=None,
        min_length=8,
        max_length=128,
    )
    is_active: bool | None = None


class UserResponse(UserBase):
    """User response schema."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    organization_id: UUID
    is_superuser: bool


class UserListResponse(BaseModel):
    """Paginated users."""

    total: int
    items: list[UserResponse]
