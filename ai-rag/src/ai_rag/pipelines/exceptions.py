"""Exceptions for pipelines."""


class PipelineError(Exception):
    """Base pipeline exception."""


class InvalidPipelineError(PipelineError):
    """Raised when a pipeline is unsupported."""


class InvalidPipelineStepError(PipelineError):
    """Raised when a pipeline step is invalid."""