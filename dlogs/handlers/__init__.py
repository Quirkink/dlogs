"""
Handlers for different log formats.
"""

from typing import TYPE_CHECKING

from dlogs.handlers.django import DjangoHandler

if TYPE_CHECKING:
    from dlogs.handlers.abc.abc_handler import ABCHandler


HANDLERS = [
    DjangoHandler,
]


def get_handler(tag: str) -> 'ABCHandler | None':
    """
    Get a handler by tag.
    """

    for handler in HANDLERS:
        if handler.tag == tag:
            return handler

    return None


def get_tags() -> list[str]:
    """
    Get all tags.
    """

    return [handler.tag for handler in HANDLERS]


__all__ = (
    'get_handler',
    'get_tags',
)
