import pytest

from homework_03.solutions import shell_sort


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, -1, 3, 3, 0], [-1, 0, 3, 3, 5]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
    ],
)
def test_shell_sort(arr, expected):
    assert shell_sort(arr) == expected
