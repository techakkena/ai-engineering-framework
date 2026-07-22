from __future__ import annotations

"""Tests for TeamRepository."""

from uuid import uuid4

import pytest

from app.models.team import Team
from app.teams.repository import TeamRepository


@pytest.fixture
def repository(db_session):
    """Create repository."""
    return TeamRepository(db_session)


@pytest.fixture
def team(db_session):
    """Create a sample team."""
    team = Team(
        organization_id=uuid4(),
        name="Engineering",
        code="ENG",
        description="Engineering Team",
    )

    db_session.add(team)
    db_session.commit()
    db_session.refresh(team)

    return team


def test_get(repository: TeamRepository, team: Team) -> None:
    """Test get by id."""
    result = repository.get(team.id)

    assert result is not None
    assert result.id == team.id


def test_get_missing(repository: TeamRepository) -> None:
    """Test get missing team."""
    assert repository.get(uuid4()) is None


def test_get_by_code(
    repository: TeamRepository,
    team: Team,
) -> None:
    """Test get by code."""
    result = repository.get_by_code(team.code)

    assert result is not None
    assert result.code == team.code


def test_get_by_name(
    repository: TeamRepository,
    team: Team,
) -> None:
    """Test get by name."""
    result = repository.get_by_name(
        organization_id=team.organization_id,
        name=team.name,
    )

    assert result is not None
    assert result.name == team.name


def test_exists_by_name(
    repository: TeamRepository,
    team: Team,
) -> None:
    """Test exists by name."""
    assert repository.exists_by_name(
        organization_id=team.organization_id,
        name=team.name,
    )


def test_exists_by_code(
    repository: TeamRepository,
    team: Team,
) -> None:
    """Test exists by code."""
    assert repository.exists_by_code(team.code)


def test_list_by_organization(
    repository: TeamRepository,
    team: Team,
) -> None:
    """Test list by organization."""
    results = repository.list_by_organization(
        team.organization_id,
    )

    assert len(results) == 1
    assert results[0].id == team.id


def test_missing_code(repository: TeamRepository) -> None:
    """Test missing code."""
    assert repository.get_by_code("UNKNOWN") is None


def test_missing_name(
    repository: TeamRepository,
    team: Team,
) -> None:
    """Test missing name."""
    assert (
        repository.get_by_name(
            organization_id=team.organization_id,
            name="Support",
        )
        is None
    )