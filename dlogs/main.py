"""
Main module for the CLI application.

The main task in the development was to reuse
the code so that this or that functionality
could be easily cut or supplemented.
After studying the poetry sources,
I rethought my "vision" of application architecture
when you can't even reuse or call this or
that functionality from regular code and you
have to rewrite it.

P.S. But this does not mean that
I do not know about such things
as SOLID or Clean Architecture.

EXAMPLE:

dlogs log/log_file.log
dlogs logs/
dlogs log/log_file.log log/log_file2.log
dlogs log/ --report django
dlogs log/ --report django --suffix .log
dlogs log/ --report django --debug
"""

from dlogs.utils.thread import ThreadPool
from dlogs.utils.path import get_files
from dlogs.utils.aparse import AParse

from dlogs.handlers import get_tags, get_handler


def main():
    """
    Main function for the CLI application.
    """

    parser = AParse()

    parser.set_handlers(
        handlers=get_tags(),
    )

    # Setting the selection of handlers by
    # the tags of all handlers
    # (a small simplification in support)

    parser.add_default_arguments()
    # Adding default arguments

    args = parser.parse_args()
    # Parsing arguments

    handler = get_handler(args.report)

    if handler is None:
        print(f'Handler {args.report} not found')

        return

    if args.debug:
        print('Start processing...\n')

    results = []

    with ThreadPool(max_workers=len(args.logs)) as pool:

        futures = []

        for log_file in get_files(args.logs, args.suffix):
            future = pool.submit(handler().handle, log_file)

            if args.debug:
                print('Handle path: ', log_file, f'({id(future)})')

            futures.append(future)

        print('\nWaiting for completion of all features...\n')

        for future in pool.as_completed(futures):
            result = future.result()
            results.append(result)

            if args.debug:
                print(f'Feature is completed: ({id(future)})')

    if args.debug:
        print('\nGenerate report...\n')

    handler.generate_report(results)


if __name__ == "__main__":
    main()
