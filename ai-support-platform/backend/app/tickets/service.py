from __future__ import annotations

"""Ticket service."""

from typing import Any, cast
from uuid import UUID

from app.core.exceptions import ResourceNotFoundException
from app.models.ticket import Ticket
from app.repositories.category import CategoryRepository
from app.repositories.priority import PriorityRepository
from app.repositories.status import StatusRepository
from app.repositories.ticket import TicketRepository
from app.repositories.user import UserRepository
from app.tickets.schemas import (
    CreateTicketRequest,
    UpdateTicketRequest,
)
from sqlalchemy.orm import Session


class TicketService:
    """Service for ticket management."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        """Initialize the ticket service."""
        self.session = session

        self.ticket_repository = TicketRepository(session)
        self.priority_repository = PriorityRepository(session)
        self.category_repository = CategoryRepository(session)
        self.status_repository = StatusRepository(session)
        self.user_repository = UserRepository(session)

    def create_ticket(
        self,
        organization_id: UUID,
        created_by_id: UUID,
        request: CreateTicketRequest,
    ) -> Ticket:
        """Create a new ticket."""
        priority = self.priority_repository.get(
            request.priority_id,
        )

        if priority is None:
            raise ResourceNotFoundException(
                "Priority not found.",
            )

        if cast(Any, priority).organization_id != organization_id:
            raise ResourceNotFoundException(
                "Priority not found.",
            )

        if request.category_id is not None:
            category = self.category_repository.get(
                request.category_id,
            )

            if category is None:
                raise ResourceNotFoundException(
                    "Category not found.",
                )

            if cast(Any, category).organization_id != organization_id:
                raise ResourceNotFoundException(
                    "Category not found.",
                )

        if request.assignee_id is not None:
            assignee = self.user_repository.get(
                request.assignee_id,
            )

            if assignee is None:
                raise ResourceNotFoundException(
                    "Assignee not found.",
                )

            if cast(Any, assignee).organization_id != organization_id:
                raise ResourceNotFoundException(
                    "Assignee not found.",
                )

        ticket = Ticket(
            organization_id=organization_id,
            created_by_id=created_by_id,
            title=request.title,
            description=request.description,
            priority_id=request.priority_id,
            category_id=request.category_id,
            assignee_id=request.assignee_id,
        )

        try:
            self.ticket_repository.create(ticket)

            self.session.commit()
            self.session.refresh(ticket)

        except Exception:
            self.session.rollback()
            raise

        return ticket

    def get_ticket(
        self,
        ticket_id: UUID,
    ) -> Ticket:
        """Return a ticket."""
        ticket = self.ticket_repository.get(
            ticket_id,
        )

        if ticket is None:
            raise ResourceNotFoundException(
                "Ticket not found.",
            )

        return ticket

    def list_tickets(
        self,
        organization_id: UUID,
    ) -> list[Ticket]:
        """Return organization tickets."""
        return self.ticket_repository.list_by_organization(
            organization_id,
        )

    def update_ticket(
        self,
        ticket_id: UUID,
        request: UpdateTicketRequest,
    ) -> Ticket:
        """Update a ticket."""
        ticket = self.get_ticket(ticket_id)

        if request.priority_id is not None:
            priority = self.priority_repository.get(
                request.priority_id,
            )

            if priority is None:
                raise ResourceNotFoundException(
                    "Priority not found.",
                )

            if cast(Any, priority).organization_id != cast(Any, ticket).organization_id:
                raise ResourceNotFoundException(
                    "Priority not found.",
                )

        if request.category_id is not None:
            category = self.category_repository.get(
                request.category_id,
            )

            if category is None:
                raise ResourceNotFoundException(
                    "Category not found.",
                )

            if cast(Any, category).organization_id != cast(Any, ticket).organization_id:
                raise ResourceNotFoundException(
                    "Category not found.",
                )

        if request.status_id is not None:
            status = self.status_repository.get(
                request.status_id,
            )

            if status is None:
                raise ResourceNotFoundException(
                    "Status not found.",
                )

            if cast(Any, status).organization_id != cast(Any, ticket).organization_id:
                raise ResourceNotFoundException(
                    "Status not found.",
                )

        if request.assignee_id is not None:
            assignee = self.user_repository.get(
                request.assignee_id,
            )

            if assignee is None:
                raise ResourceNotFoundException(
                    "Assignee not found.",
                )

            if cast(Any, assignee).organization_id != cast(Any, ticket).organization_id:
                raise ResourceNotFoundException(
                    "Assignee not found.",
                )

        updates = request.model_dump(
            exclude_unset=True,
        )

        for field, value in updates.items():
            setattr(
                ticket,
                field,
                value,
            )

        try:
            self.session.commit()
            self.session.refresh(ticket)

        except Exception:
            self.session.rollback()
            raise

        return ticket

    def delete_ticket(
        self,
        ticket_id: UUID,
    ) -> None:
        """Delete a ticket."""
        ticket = self.get_ticket(ticket_id)

        try:
            self.ticket_repository.delete(ticket)

            self.session.commit()

        except Exception:
            self.session.rollback()
            raise