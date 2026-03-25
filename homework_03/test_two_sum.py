from homework_03.solutions import two_sum


def test_two_sum_classic_case():
    assert two_sum([2, 7, 11, 15], 9) == [1, 0]


def test_two_sum_with_duplicates():
    assert two_sum([3, 3], 6) == [1, 0]


def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 100) == []
