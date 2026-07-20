from __future__ import annotations

"""Ticket schemas."""

from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

Title = Annotated[
    str,
    Field(
        min_length=3,
        max_length=200,
    ),
]

Description = Annotated[
    str,
    Field(
        min_length=1,
        max_length=10000,
    ),
]


class CreateTicketRequest(BaseModel):
    """Request model for creating a ticket."""

    title: Title
    description: Description
    priority_id: UUID
    category_id: UUID | None = None
    assignee_id: UUID | None = None


class UpdateTicketRequest(BaseModel):
    """Request model for updating a ticket."""

    title: Title | None = None
    description: Description | None = None
    priority_id: UUID | None = None
    category_id: UUID | None = None
    assignee_id: UUID | None = None
    status_id: UUID | None = None


class TicketResponse(BaseModel):
    """Ticket response."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID
    organization_id: UUID

    ticket_number: str

    title: str
    description: str

    priority_id: UUID
    category_id: UUID | None
    status_id: UUID
    assignee_id: UUID | None

    created_by_id: UUID

    created_at: datetime
    updated_at: datetime


class TicketListResponse(BaseModel):
    """Ticket list response."""

    tickets: list[TicketResponse]

    total: int