from __future__ import annotations

"""Tests for ticket service."""

from uuid import uuid4

import pytest

from app.core.exceptions import (
    ConflictException,
    ResourceNotFoundException,
)
from app.tickets.repository import TicketRepository
from app.tickets.schemas import (
    CreateTicketRequest,
    UpdateTicketRequest,
)
from app.tickets.service import TicketService


@pytest.fixture
def ticket_service(
    ticket_repository: TicketRepository,
) -> TicketService:
    """Return ticket service."""
    return TicketService(ticket_repository)


def test_create_ticket(
    ticket_service: TicketService,
    organization,
    user,
) -> None:
    """Create ticket."""
    request = CreateTicketRequest(
        organization_id=organization.id,
        created_by=user.id,
        assigned_to=user.id,
        title="Printer Issue",
        description="Printer is offline.",
        priority="medium",
        status="open",
    )

    ticket = ticket_service.create_ticket(request)

    assert ticket.id is not None
    assert ticket.title == "Printer Issue"


def test_duplicate_title(
    ticket_service: TicketService,
    organization,
    user,
) -> None:
    """Duplicate titles are rejected."""
    request = CreateTicketRequest(
        organization_id=organization.id,
        created_by=user.id,
        assigned_to=user.id,
        title="Duplicate",
        description="Description",
        priority="medium",
        status="open",
    )

    ticket_service.create_ticket(request)

    with pytest.raises(ConflictException):
        ticket_service.create_ticket(request)


def test_get_ticket(
    ticket_service: TicketService,
    organization,
    user,
) -> None:
    """Return ticket."""
    created = ticket_service.create_ticket(
        CreateTicketRequest(
            organization_id=organization.id,
            created_by=user.id,
            assigned_to=user.id,
            title="Login Issue",
            description="Cannot login.",
            priority="high",
            status="open",
        )
    )

    ticket = ticket_service.get_ticket(created.id)

    assert ticket.id == created.id


def test_get_missing_ticket(
    ticket_service: TicketService,
) -> None:
    """Missing ticket raises."""
    with pytest.raises(ResourceNotFoundException):
        ticket_service.get_ticket(uuid4())


def test_list_tickets(
    ticket_service: TicketService,
    organization,
    user,
) -> None:
    """List tickets."""
    for index in range(3):
        ticket_service.create_ticket(
            CreateTicketRequest(
                organization_id=organization.id,
                created_by=user.id,
                assigned_to=user.id,
                title=f"Ticket {index}",
                description="Description",
                priority="medium",
                status="open",
            )
        )

    tickets = ticket_service.list_tickets()

    assert len(tickets) >= 3


def test_update_ticket(
    ticket_service: TicketService,
    organization,
    user,
) -> None:
    """Update ticket."""
    created = ticket_service.create_ticket(
        CreateTicketRequest(
            organization_id=organization.id,
            created_by=user.id,
            assigned_to=user.id,
            title="Old Title",
            description="Old Description",
            priority="medium",
            status="open",
        )
    )

    updated = ticket_service.update_ticket(
        created.id,
        UpdateTicketRequest(
            title="New Title",
            description="New Description",
            priority="high",
            status="closed",
        ),
    )

    assert updated.title == "New Title"
    assert updated.description == "New Description"


def test_delete_ticket(
    ticket_service: TicketService,
    organization,
    user,
) -> None:
    """Delete ticket."""
    created = ticket_service.create_ticket(
        CreateTicketRequest(
            organization_id=organization.id,
            created_by=user.id,
            assigned_to=user.id,
            title="Delete Ticket",
            description="Delete me.",
            priority="medium",
            status="open",
        )
    )

    ticket_service.delete_ticket(created.id)

    with pytest.raises(ResourceNotFoundException):
        ticket_service.get_ticket(created.id)
