"""
Framework-independent CI/CD operations.
"""

from __future__ import annotations

from dataclasses import dataclass

from ai_deployment.ci_cd.constants import (
    DEFAULT_BRANCH,
    DEFAULT_PIPELINE_NAME,
    DEFAULT_TRIGGER,
)
from ai_deployment.ci_cd.exceptions import (
    CICDConfigurationError,
    CICDPipelineError,
)


@dataclass(slots=True, frozen=True)
class Pipeline:
    """Represents a CI/CD pipeline."""

    name: str = DEFAULT_PIPELINE_NAME
    branch: str = DEFAULT_BRANCH
    trigger: str = DEFAULT_TRIGGER


class PipelineService:
    """Framework-independent CI/CD service."""

    def run(
        self,
        pipeline: Pipeline,
    ) -> bool:
        """Run a pipeline."""
        if not pipeline.name.strip():
            raise CICDConfigurationError(
                "Pipeline name cannot be empty."
            )

        return True

    def validate(
        self,
        pipeline: Pipeline,
    ) -> bool:
        """Validate a pipeline configuration."""
        if not pipeline.branch.strip():
            raise CICDConfigurationError(
                "Branch cannot be empty."
            )

        return True

    def cancel(
        self,
        pipeline: Pipeline,
    ) -> bool:
        """Cancel a running pipeline."""
        if not pipeline.name.strip():
            raise CICDPipelineError(
                "Pipeline name cannot be empty."
            )

        return True