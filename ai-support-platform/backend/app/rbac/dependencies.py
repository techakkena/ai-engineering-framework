"""RBAC dependencies."""

from __future__ import annotations

from collections.abc import Callable, Coroutine
from typing import Annotated, Any

from fastapi import Depends, HTTPException

from app.auth.dependencies import CurrentActiveUserDependency
from app.core.dependencies import DatabaseDependency
from app.models.user import User
from app.rbac.service import RBACService


def get_rbac_service(
    db: DatabaseDependency,
) -> RBACService:
    """Return an RBAC service."""
    return RBACService(db)


RBACServiceDependency = Annotated[
    RBACService,
    Depends(get_rbac_service),
]


def require_permission(
    resource: str,
    action: str,
) -> Callable[[CurrentActiveUserDependency, RBACService], Coroutine[Any, Any, User]]:
    """Factory that returns a dependency checking for specific resource permissions."""

    async def dependency(
        current_user: CurrentActiveUserDependency,
        rbac_service: Annotated[RBACService, Depends(get_rbac_service)],
    ) -> User:
        # Pass current_user.id instead of current_user
        if not rbac_service.has_permission(current_user.id, resource, action):
            raise HTTPException(status_code=403, detail="Permission Denied")
        return current_user

    # Add this line at the outer level to return the inner dependency function
    return dependency