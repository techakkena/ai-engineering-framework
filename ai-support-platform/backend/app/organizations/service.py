from __future__ import annotations

"""Organization service."""

from uuid import UUID

from app.core.exceptions import (
    ConflictException,
    ResourceNotFoundException,
)
from app.models.organization import Organization
from app.organizations.schemas import (
    CreateOrganizationRequest,
    UpdateOrganizationRequest,
)
from app.repositories.organization import OrganizationRepository


class OrganizationService:
    """Service for organization management."""

    def __init__(
        self,
        repository: OrganizationRepository,
    ) -> None:
        """Initialize the service.

        Args:
            repository: Organization repository.
        """
        self.repository = repository

    def create_organization(
        self,
        request: CreateOrganizationRequest,
    ) -> Organization:
        """Create a new organization.

        Args:
            request: Organization creation request.

        Returns:
            Created organization.

        Raises:
            ConflictException: If the name or code already exists.
        """
        if self.repository.exists_by_name(request.name):
            raise ConflictException(
                "Organization name already exists.",
            )

        if self.repository.exists_by_code(request.code):
            raise ConflictException(
                "Organization code already exists.",
            )

        organization = self.repository.create(
            Organization(
                name=request.name,
                code=request.code,
                email=request.email,
                phone=request.phone,
                website=str(request.website)
                if request.website
                else None,
            )
        )

        self.repository.session.commit()
        self.repository.session.refresh(organization)

        return organization

    def get_organization(
        self,
        organization_id: UUID,
    ) -> Organization:
        """Return an organization by ID.

        Args:
            organization_id: Organization identifier.

        Returns:
            Organization instance.

        Raises:
            ResourceNotFoundException: If the organization does not exist.
        """
        organization = self.repository.get_by_id(
            organization_id,
        )

        if organization is None:
            raise ResourceNotFoundException(
                "Organization not found.",
            )

        return organization

    def list_organizations(
        self,
    ) -> list[Organization]:
        """Return all organizations.

        Returns:
            List of organizations.
        """
        return self.repository.list()

    def update_organization(
        self,
        organization_id: UUID,
        request: UpdateOrganizationRequest,
    ) -> Organization:
        """Update an organization.

        Args:
            organization_id: Organization identifier.
            request: Update request.

        Returns:
            Updated organization.
        """
        organization = self.get_organization(
            organization_id,
        )

        if (
            request.name
            and request.name != organization.name
        ):
            if self.repository.exists_by_name(request.name):
                raise ConflictException(
                    "Organization name already exists.",
                )
            organization.name = request.name

        if (
            request.code
            and request.code != organization.code
        ):
            if self.repository.exists_by_code(request.code):
                raise ConflictException(
                    "Organization code already exists.",
                )
            organization.code = request.code

        if request.email is not None:
            organization.email = request.email

        if request.phone is not None:
            organization.phone = request.phone

        if request.website is not None:
            organization.website = str(request.website)

        if request.is_active is not None:
            organization.is_active = request.is_active

        self.repository.session.commit()
        self.repository.session.refresh(organization)

        return organization

    def delete_organization(
        self,
        organization_id: UUID,
    ) -> None:
        """Soft-delete an organization.

        Args:
            organization_id: Organization identifier.
        """
        organization = self.get_organization(
            organization_id,
        )

        organization.soft_delete()

        self.repository.session.commit()