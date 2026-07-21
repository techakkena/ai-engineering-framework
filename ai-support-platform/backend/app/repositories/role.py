from __future__ import annotations

"""Role repository."""

from uuid import UUID

from app.models.role import Role
from app.repositories.base import BaseRepository
from sqlalchemy import select
from sqlalchemy.orm import Session


class RoleRepository(BaseRepository[Role]):
    """Repository for role entities."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        super().__init__(
            session=session,
            model=Role,
        )

    def get_by_name(
        self,
        organization_id: UUID,
        name: str,
    ) -> Role | None:
        statement = select(Role).where(
            Role.organization_id == organization_id,
            Role.name == name,
            Role.is_deleted.is_(False),
        )

        return self.session.scalar(statement)

    def exists_by_name(
        self,
        organization_id: UUID,
        name: str,
    ) -> bool:
        return (
            self.get_by_name(
                organization_id,
                name,
            )
            is not None
        )

    def list_by_organization(
        self,
        organization_id: UUID,
    ) -> list[Role]:
        statement = (
            select(Role)
            .where(
                Role.organization_id == organization_id,
                Role.is_deleted.is_(False),
            )
            .order_by(Role.name.asc())
        )

        return list(
            self.session.scalars(statement).all(),
        )
