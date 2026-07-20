from __future__ import annotations

from pathlib import Path

from .constants import DEFAULT_ENCODING
from .exceptions import FileSystemToolError


class FileSystemTool:
    """Simple filesystem helper."""

    def exists(
        self,
        path: str | Path,
    ) -> bool:
        """Return whether a file exists."""
        return Path(path).exists()

    def read_text(
        self,
        path: str | Path,
    ) -> str:
        """Read a UTF-8 text file."""

        try:
            return Path(path).read_text(
                encoding=DEFAULT_ENCODING,
            )
        except OSError as exc:
            raise FileSystemToolError(
                str(exc),
            ) from exc

    def write_text(
        self,
        path: str | Path,
        content: str,
    ) -> None:
        """Write a UTF-8 text file."""

        try:
            Path(path).write_text(
                content,
                encoding=DEFAULT_ENCODING,
            )
        except OSError as exc:
            raise FileSystemToolError(
                str(exc),
            ) from exc
