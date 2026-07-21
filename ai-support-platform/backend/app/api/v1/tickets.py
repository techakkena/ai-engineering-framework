from __future__ import annotations

"""Ticket API."""

from typing import Annotated
from uuid import UUID

from app.auth.dependencies import get_current_user
from app.models.user import User
from app.tickets.dependencies import get_ticket_service
from app.tickets.schemas import (
    CreateTicketRequest,
    TicketListResponse,
    TicketResponse,
    UpdateTicketRequest,
)
from app.tickets.service import TicketService
from fastapi import APIRouter, Depends, Response, status

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"],
)

CurrentUserDependency = Annotated[
    User,
    Depends(get_current_user),
]

TicketServiceDependency = Annotated[
    TicketService,
    Depends(get_ticket_service),
]


@router.get(
    "",
    response_model=TicketListResponse,
)
@router.get("", response_model=TicketListResponse)
def list_tickets(
    service: TicketServiceDependency,
) -> TicketListResponse:

    tickets = service.list_tickets()

    return TicketListResponse(
        total=len(tickets),
        tickets=tickets,
    )


@router.get(
    "/{ticket_id}",
    response_model=TicketResponse,
)
def get_ticket(
    ticket_id: UUID,
    service: TicketServiceDependency,
    _: CurrentUserDependency,
) -> TicketResponse:
    """Return ticket."""
    return service.get_ticket(ticket_id)


@router.post(
    "",
    response_model=TicketResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_ticket(
    request: CreateTicketRequest,
    service: TicketServiceDependency,
    _: CurrentUserDependency,
) -> TicketResponse:
    """Create ticket."""
    return service.create_ticket(request)


@router.patch(
    "/{ticket_id}",
    response_model=TicketResponse,
)
def update_ticket(
    ticket_id: UUID,
    request: UpdateTicketRequest,
    service: TicketServiceDependency,
    _: CurrentUserDependency,
) -> TicketResponse:
    """Update ticket."""
    return service.update_ticket(
        ticket_id,
        request,
    )


@router.delete(
    "/{ticket_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_ticket(
    ticket_id: UUID,
    service: TicketServiceDependency,
    _: CurrentUserDependency,
) -> Response:
    """Delete ticket."""
    service.delete_ticket(ticket_id)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
