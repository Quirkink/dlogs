"""
Abstract base class for handlers.

It is assumed that to create your own handler,
you inherit from this abstract handler.
"""

from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any
    from dlogs.dto.log import DTOLog


class ABCHandler(ABC):
    """
    Abstract base class for handlers.
    """

    tag: str
    # Tag for the handler (helping to find the handler)

    @abstractmethod
    def parse_log_object(self, line: str) -> 'DTOLog | None':
        """
        Parse the log object from the line.

        :param line: The line to parse the log object from.
        :return: The log object.
        """

        raise NotImplementedError

    @abstractmethod
    def handle(self, log_file: str) -> 'Any':
        """
        Handle the log file.

        :param log_file: The log file to handle.
        :return: The list of log objects.
        """

        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def generate_report(*args: 'Any', **kwargs: 'Any') -> 'Any':
        """
        Generate the report.

        :param args: The arguments.
        :param kwargs: The keyword arguments.
        :return: The report.
        """

        raise NotImplementedError


__all__ = (
    'ABCHandler',
)
