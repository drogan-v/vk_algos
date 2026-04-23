from homework_06.solutions import coin_change


def test_coin_change_zero_amount():
    assert coin_change([1, 2, 5], 0) == 0


def test_coin_change_classic_case():
    assert coin_change([1, 2, 5], 11) == 3


def test_coin_change_impossible_case():
    assert coin_change([2], 3) == -1


def test_coin_change_single_coin_exact_match():
    assert coin_change([7], 14) == 2


def test_coin_change_prefers_optimal_not_greedy():
    assert coin_change([1, 3, 4], 6) == 2
