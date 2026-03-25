import pytest

from homework_03.solutions import binary_search_square_root


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (1, 1),
        (4, 2),
        (16, 4),
        (8, 2),
        (15, 3),
    ],
)
def test_binary_search_square_root(x, expected):
    assert binary_search_square_root(x) == expected
