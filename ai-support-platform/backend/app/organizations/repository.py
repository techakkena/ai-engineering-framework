from __future__ import annotations

"""Organization repository implementation."""

from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.repositories.base import BaseRepository


class OrganizationRepository(BaseRepository[Organization]):
    """Repository for managing Organization database operations."""

    def __init__(self, session: Session) -> None:
        """Initialize repository with the Organization model context."""
        super().__init__(session, Organization)