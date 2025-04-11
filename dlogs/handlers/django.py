"""
Handler for Django logs.

The Django log format is as follows:

2025-03-28 12:32:03,000 INFO django.request: GET /example/path/ 200 OK [IP]
2025-03-28 12:32:03,000 ERROR django.request: GET /example/path/ ...

2025-03-28 12:32:03,000 DEBUG django.function: Message
2025-03-28 12:32:03,000 WARNING django.function: Message
2025-03-28 12:32:03,000 CRITICAL django.function: Message
"""

from typing import TYPE_CHECKING

from pathlib import Path
from re import compile as compile_regex

from dlogs.handlers.abc.abc_handler import ABCHandler
from dlogs.dto.log import DTOLog

if TYPE_CHECKING:
    from typing import Any


class DjangoHandler(ABCHandler):
    """
    Handler for Django logs.

    This handler is used to count the number of requests
    for each path and level.
    """

    tag = 'django'
    # Tag for the handler (helping to find the handler)

    log_pattern = compile_regex(
        r'(\d+-\d+-\d+ \d+:\d+:\d+,\d+) (\w+) (.*?:) (.*)?',
    )
    # Pattern for the log line

    info_pattern = compile_regex(
        r'(\S+) (\S+) (\d+) (\S+) (\S+)'
    )
    # Pattern for the info log line

    error_pattern = compile_regex(
        r'^(.*?:) (/.*?) '
    )
    # Pattern for the error log line

    def __init__(self):
        """
        Initialize the handler.
        """

        self.logs: list[list[DTOLog, int]] = []

    def find_log_object(self, log_object: DTOLog) -> list[DTOLog, int] | None:
        """
        Find the log object in the logs.

        :param log_object: The log object to find.
        :return: The log object.
        """

        for log in self.logs:

            if (log[0].level == log_object.level) and (
                log[0].url_path == log_object.url_path
            ):
                return log

        return None

    def parse_log_object(self, line: str) -> DTOLog | None:
        """
        Parse the log object from the line.

        :param line: The line to get the log object from.
        :return: The log object.
        """

        log_match = self.log_pattern.match(line)
        # Matching the log line

        if log_match is None:
            # If the log line is not matched, return None

            return None

        level = log_match.group(2)
        # Getting the level

        url_path = None
        # Initializing the url path

        if level.lower() == 'info':
            # If the level is INFO, find the url path

            if info_match := self.info_pattern.match(log_match.group(4)):
                url_path = info_match.group(2)

        if level.lower() == 'error':
            # If the level is ERROR, find the url path

            if error_match := self.error_pattern.match(log_match.group(4)):
                url_path = error_match.group(2)

        # Returning the log object
        return DTOLog(
            level=level,
            url_path=url_path,
        )

    def handle(self, log_file: Path) -> list[list[DTOLog, int]]:
        """
        Handle the log file.

        :param log_file: The log file to handle.
        :return: The logs.
        """

        with open(log_file, 'r', encoding='utf-8') as file:

            for line in file:

                log_object = self.parse_log_object(line)

                if log_object is None:
                    continue

                log = self.find_log_object(log_object)

                if log is None:
                    self.logs.append([log_object, 1])

                else:
                    log[1] += 1

        return self.logs

    @staticmethod
    def generate_report(
        logs: list[list[list[DTOLog, int]]],
        *args: 'Any',
        **kwargs: 'Any',
    ) -> None:
        """
        Generate the report.

        :param logs: The logs.
        :param args: The arguments.
        """

        # Merging logs from multiple files
        path_level_counts = {}

        # Collect counts by path and level
        for list_log in logs:
            # list_log: list[list[DTOLog, int]]

            for log_object, count in list_log:
                # log_object: DTOLog
                # count: int

                path = log_object.url_path or 'None'
                level = log_object.level

                if path not in path_level_counts:
                    path_level_counts[path] = {
                        'DEBUG': 0,
                        'INFO': 0,
                        'WARNING': 0,
                        'ERROR': 0,
                        'CRITICAL': 0,
                    }

                path_level_counts[path][level] += count

        # Print the report with new format
        header = (
            f'{"PATH":<30} | {"DEBUG":<8} | {"INFO":<8} | '
            f'{"WARNING":<8} | {"ERROR":<8} | {"CRITICAL":<8}'
        )

        print(header)
        print('-' * len(header))

        # Sort paths alphabetically for consistent output
        for path in sorted(path_level_counts.keys()):

            counts = path_level_counts[path]

            print(
                f'{path:<30} | {counts["DEBUG"]:<8} | {counts["INFO"]:<8} | '
                f'{counts["WARNING"]:<8} | {counts["ERROR"]:<8} | '
                f'{counts["CRITICAL"]:<8}'
            )

        # Calculate total requests across all paths and levels
        total_requests = sum(
            sum(counts.values())
            for counts in path_level_counts.values()
        )

        print('-' * len(header))
        print(f'Total requests: {total_requests}')
        print('-' * len(header))


__all__ = (
    'DjangoHandler',
)
