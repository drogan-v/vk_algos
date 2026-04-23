from homework_06.solutions import find_LIS


def test_find_lis_empty_array():
    assert find_LIS([]) == 0


def test_find_lis_single_element():
    assert find_LIS([42]) == 1


def test_find_lis_strictly_increasing():
    assert find_LIS([1, 2, 3, 4, 5]) == 5


def test_find_lis_strictly_decreasing():
    assert find_LIS([5, 4, 3, 2, 1]) == 1


def test_find_lis_with_drop_inside_sequence():
    assert find_LIS([1, 2, 3, 0, 1, 2]) == 3
