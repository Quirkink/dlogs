"""
Argument parser for the application.

The usual simplifying utility,
I thought why not put it in a
separate file to work with this
module right here, it's certainly
easy to maintain.
"""

from argparse import ArgumentParser
from sys import argv, exit as sys_exit


APPLICATION_DESCRIPTION = 'A tool for analyzing and reporting on log files.'

LOGS_HELP = 'Path to log files, can be specified multiple times'
REPORT_HELP = 'The name of the handler that will be used to generate the report'
SUFFIX_HELP = 'The suffix of the log files'


class AParse:
    """
    Argument parser for the application.

    TODO: i need writing library in the likeness
    of click, type, questionary for WeretCLI
    """

    def __init__(self) -> None:
        """
        Initialize the argument parser.
        """

        self.handlers = []

        self.parser: ArgumentParser = ArgumentParser(
            description=APPLICATION_DESCRIPTION,
        )

    @property
    def argument_parser(self):
        """
        Get the argument parser.
        """

        return self.parser

    def set_handlers(self, handlers: list[str]):
        """
        Set the handlers.
        """

        self.handlers = handlers

    def add_default_arguments(self):
        """
        Add the default arguments to the argument parser.
        """

        self.parser.add_argument(
            'logs',
            type=str,
            nargs='+',
            help=LOGS_HELP,
        )
        # Paths to the log files.

        self.parser.add_argument(
            '--report',
            type=str,
            required=False,
            default=self.handlers[0],
            help=REPORT_HELP,
            choices=self.handlers,
        )
        # The name of the handler that will be used to generate the report.

        self.parser.add_argument(
            '--suffix',
            type=str,
            required=False,
            default=None,
            help=SUFFIX_HELP,
        )
        # The suffix of the log files.
        # If not specified, all log files will be used.

        self.parser.add_argument(
            '--debug',
            action='store_true',
            help='Enable debug output',
            default=False,
        )
        # Enable debug output.

    def parse_args(self):
        """
        Parse the arguments.
        """

        if len(argv) == 1:

            self.parser.print_help()
            sys_exit(0)

        return self.parser.parse_args()


__all__ = (
    'AParse',
)
