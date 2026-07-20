from __future__ import annotations

"""Organization API schemas."""

from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, HttpUrl


class CreateOrganizationRequest(BaseModel):
    """Request model for creating an organization."""

    name: str = Field(
        min_length=2,
        max_length=255,
    )

    code: str = Field(
        min_length=2,
        max_length=50,
    )

    email: EmailStr | None = None

    phone: str | None = Field(
        default=None,
        max_length=25,
    )

    website: HttpUrl | None = None


class UpdateOrganizationRequest(BaseModel):
    """Request model for updating an organization."""

    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=255,
    )

    code: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
    )

    email: EmailStr | None = None

    phone: str | None = Field(
        default=None,
        max_length=25,
    )

    website: HttpUrl | None = None

    is_active: bool | None = None


class OrganizationResponse(BaseModel):
    """Organization response model."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    name: str

    code: str

    email: EmailStr | None

    phone: str | None

    website: HttpUrl | None

    is_active: bool


class OrganizationListResponse(BaseModel):
    """Organization list response."""

    organizations: list[OrganizationResponse]