"""
This module contains the DTO for the log.

It is assumed that all DTOs related to
logs will be implemented in this file.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class DTOLog:
    """
    DTO for the log.
    """

    level: str
    url_path: str | None


__all__ = (
    'DTOLog',
)
