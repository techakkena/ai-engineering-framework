"""Tests for the AI Knowledge router."""

from __future__ import annotations

from uuid import uuid4

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.ai.knowledge.models import KnowledgeBase
from app.models.organization import Organization
from app.models.user import User


def test_create_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test creating a knowledge base."""
    response = client.post(
        "/api/v1/knowledge",
        json={
            "name": "Support KB",
            "description": "Knowledge Base",
            "visibility": "private",
            "metadata": {},
        },
        headers=auth_headers,
    )

    assert response.status_code == 201

    data = response.json()

    assert data["organization_id"] == str(organization.id)
    assert data["name"] == "Support KB"
    assert data["description"] == "Knowledge Base"
    assert data["visibility"] == "private"


def test_list_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test listing knowledge bases."""
    knowledge = KnowledgeBase(
        organization_id=organization.id,
        name="KB1",
        description="Description",
        created_by=user.id,
        updated_by=user.id,
    )

    db_session.add(knowledge)
    db_session.commit()

    response = client.get(
        "/api/v1/knowledge",
        headers=auth_headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["total"] >= 1
    assert len(data["items"]) >= 1


def test_get_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test retrieving a knowledge base."""
    knowledge = KnowledgeBase(
        organization_id=organization.id,
        name="Support",
        description="Description",
        created_by=user.id,
        updated_by=user.id,
    )

    db_session.add(knowledge)
    db_session.commit()
    db_session.refresh(knowledge)

    response = client.get(
        f"/api/v1/knowledge/{knowledge.id}",
        headers=auth_headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(knowledge.id)
    assert data["organization_id"] == str(organization.id)
    assert data["name"] == "Support"
    assert data["description"] == "Description"


def test_get_knowledge_not_found(
    client: TestClient,
    auth_headers: dict[str, str],
) -> None:
    """Test retrieving a missing knowledge base."""
    response = client.get(
        f"/api/v1/knowledge/{uuid4()}",
        headers=auth_headers,
    )

    assert response.status_code == 404

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Knowledge base not found."
    assert data["error_code"] == "KnowledgeNotFoundError"
    assert data["details"] is None
    assert "metadata" in data
    assert "timestamp" in data["metadata"]


def test_update_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test updating a knowledge base."""
    knowledge = KnowledgeBase(
        organization_id=organization.id,
        name="Old Name",
        created_by=user.id,
        updated_by=user.id,
    )

    db_session.add(knowledge)
    db_session.commit()
    db_session.refresh(knowledge)

    response = client.patch(
        f"/api/v1/knowledge/{knowledge.id}",
        json={
            "name": "New Name",
        },
        headers=auth_headers,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == str(knowledge.id)
    assert data["name"] == "New Name"


def test_delete_knowledge(
    client: TestClient,
    auth_headers: dict[str, str],
    organization: Organization,
    user: User,
    db_session: Session,
) -> None:
    """Test deleting a knowledge base."""
    knowledge = KnowledgeBase(
        organization_id=organization.id,
        name="Delete Me",
        created_by=user.id,
        updated_by=user.id,
    )

    db_session.add(knowledge)
    db_session.commit()
    db_session.refresh(knowledge)

    knowledge_id = knowledge.id

    response = client.delete(
        f"/api/v1/knowledge/{knowledge_id}",
        headers=auth_headers,
    )

    assert response.status_code == 204

    db_session.expire_all()

    deleted = db_session.get(
        KnowledgeBase,
        knowledge_id,
    )

    assert deleted is None


def test_delete_knowledge_not_found(
    client: TestClient,
    auth_headers: dict[str, str],
) -> None:
    """Test deleting a missing knowledge base."""
    response = client.delete(
        f"/api/v1/knowledge/{uuid4()}",
        headers=auth_headers,
    )

    assert response.status_code == 404

    data = response.json()

    assert data["success"] is False
    assert data["message"] == "Knowledge base not found."
    assert data["error_code"] == "KnowledgeNotFoundError"
    assert data["details"] is None
    assert "metadata" in data
    assert "timestamp" in data["metadata"]
