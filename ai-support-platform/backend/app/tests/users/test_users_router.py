from __future__ import annotations

"""Tests for Users API router."""

from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.v1.users import (
    get_user_service,
    router,
)
from app.auth.dependencies import get_current_user
from app.core.exceptions import (
    ConflictException,
    ResourceNotFoundException,
)
from app.models.user import User

app = FastAPI()
app.include_router(router, prefix="/api/v1")


class TestUsersRouter:
    """Tests for the Users router."""

    @pytest.fixture
    def client(self) -> TestClient:
        """Return a FastAPI test client."""
        return TestClient(app)

    @pytest.fixture
    def current_user(self) -> MagicMock:
        """Return a mocked authenticated user."""
        user = MagicMock(spec=User)

        user.id = uuid4()
        user.organization_id = uuid4()
        user.email = "john@example.com"
        user.username = "john"
        user.full_name = "John Doe"
        user.is_active = True
        user.is_superuser = False

        return user

    @pytest.fixture
    def user_service(self) -> MagicMock:
        """Return mocked user service."""
        return MagicMock()

    def test_list_users(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Return users."""
        user_service.list_users.return_value = [current_user]

        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.get("/api/v1/users")
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 200

        body = response.json()

        assert len(body["users"]) == 1
        assert body["users"][0]["email"] == current_user.email

    def test_get_user(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Return a user."""
        user_service.get_user.return_value = current_user

        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.get(
                f"/api/v1/users/{current_user.id}",
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 200
        assert response.json()["email"] == current_user.email

    def test_get_user_not_found(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Unknown user."""
        user_service.get_user.side_effect = ResourceNotFoundException(
            "User not found.",
        )

        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.get(
                f"/api/v1/users/{uuid4()}",
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 404

    def test_create_user(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Create a user."""
        user_service.create_user.return_value = current_user

        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.post(
                "/api/v1/users",
                json={
                    "email": current_user.email,
                    "username": current_user.username,
                    "full_name": current_user.full_name,
                    "password": "Password123!",
                    "organization_id": str(
                        current_user.organization_id,
                    ),
                },
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 201

    def test_create_duplicate_email(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Duplicate email."""
        user_service.create_user.side_effect = ConflictException(
            "Email already exists.",
        )

        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.post(
                "/api/v1/users",
                json={
                    "email": current_user.email,
                    "username": "another",
                    "full_name": "Another User",
                    "password": "Password123!",
                    "organization_id": str(
                        current_user.organization_id,
                    ),
                },
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code in (
            400,
            409,
        )

    def test_update_user(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Update a user."""
        updated = MagicMock(spec=User)

        updated.id = current_user.id
        updated.organization_id = current_user.organization_id
        updated.email = current_user.email
        updated.username = current_user.username
        updated.full_name = "Updated Name"
        updated.is_active = True
        updated.is_superuser = False

        user_service.update_user.return_value = updated

        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.patch(
                f"/api/v1/users/{current_user.id}",
                json={
                    "full_name": "Updated Name",
                },
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 200
        assert response.json()["full_name"] == "Updated Name"

    def test_delete_user(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Delete a user."""
        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.delete(
                f"/api/v1/users/{current_user.id}",
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 204

    def test_requires_authentication(
        self,
        client: TestClient,
    ) -> None:
        """Authentication required."""
        response = client.get("/api/v1/users")

        assert response.status_code in (
            401,
            403,
        )

    def test_validation_error(
        self,
        client: TestClient,
        current_user: User,
        user_service: MagicMock,
    ) -> None:
        """Validation error."""
        app.dependency_overrides[get_current_user] = lambda: current_user
        app.dependency_overrides[get_user_service] = lambda: user_service

        try:
            response = client.post(
                "/api/v1/users",
                json={},
            )
        finally:
            app.dependency_overrides.clear()

        assert response.status_code == 422
