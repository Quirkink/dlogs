from time import sleep

from dlogs.utils.thread import ThreadPool


def mock_function():
    """
    Mock function.

    :return: The result of the function.
    """

    sleep(1)

    return 1


def test_create_thread_pool():
    """
    Test the creation of a thread pool.
    """

    with ThreadPool(max_workers=1) as pool:
        assert pool is not None


def test_submit_task():
    """
    Test the submission of a task.
    """

    with ThreadPool(max_workers=1) as pool:

        future = pool.submit(mock_function)

        assert future is not None


def test_get_results():
    """
    Test the submission of a task.
    """

    with ThreadPool(max_workers=1) as pool:

        future = pool.submit(mock_function)

        result = future.result()

        assert result == 1


def test_as_completed():
    """
    Test the submission of a task with arguments.
    """

    futures = []

    with ThreadPool(max_workers=1) as pool:

        futures.append(pool.submit(mock_function))

        for future in pool.as_completed(futures):
            assert future.result() == 1


__all__ = (
    'test_create_thread_pool',
    'test_submit_task',
    'test_get_results',
)
