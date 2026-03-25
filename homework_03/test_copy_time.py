import pytest

from homework_03.solutions import copy_time


@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (1, 1, 2, 1),
        (2, 1, 2, 2),
        (4, 1, 1, 3),
        (5, 2, 3, 8),
        (6, 3, 5, 13),
    ],
)
def test_copy_time(n, x, y, expected):
    assert copy_time(n, x, y) == expected
