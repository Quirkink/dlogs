"""
Auxiliary utilities for working with threads.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Callable, Any, Iterator
    from concurrent.futures import Future


class ThreadPool:
    """
    Thread pool for parallel execution of tasks.
    """

    def __init__(self, max_workers: int = 10):
        """
        Initialize the thread pool.

        :param max_workers: The maximum number of workers.
        """

        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def __enter__(self) -> 'ThreadPool':
        """
        Enter the context.

        :return: The thread pool.
        """

        return self

    def __exit__(
        self,
        exc_type: Exception | None,
        exc_value: Exception | None,
        traceback: object | None,
    ) -> None:
        """
        Exit the context.

        :param exc_type: The type of the exception.
        :param exc_value: The value of the exception.
        :param traceback: The traceback of the exception.
        """

        self.executor.shutdown(wait=True)

    def submit(
        self,
        func: 'Callable',
        *args: 'Any',
        **kwargs: 'Any',
    ) -> 'Future':
        """
        Submit a task to the thread pool.

        :param func: The function to execute.
        :param args: The arguments to pass to the function.
        :param kwargs: The keyword arguments to pass to the function.

        :return: The future of the task.
        """

        return self.executor.submit(func, *args, **kwargs)

    def as_completed(
        self,
        futures: 'list[Future]',
    ) -> 'Iterator[Future]':
        """
        Get the results of the tasks as they complete.

        :param futures: The futures of the tasks.

        :return: The results of the tasks.
        """

        return as_completed(futures)


__all__ = (
    'ThreadPool',
)
