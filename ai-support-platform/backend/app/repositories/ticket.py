"""Defines the ticket repository."""

from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.ticket import Ticket
from app.repositories.base import BaseRepository


class TicketRepository(BaseRepository[Ticket]):
    """Repository for ticket entities."""

    def __init__(self, session: Session) -> None:
        """Initialize the ticket repository."""
        super().__init__(session, Ticket)
