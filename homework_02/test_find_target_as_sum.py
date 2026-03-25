from homework_02.solutions import find_target_as_sum


def test_empty_array():
    """Пустой массив не может содержать пару"""
    assert find_target_as_sum([], 5) is False


def test_single_element():
    """Массив из одного элемента не может содержать пару"""
    assert find_target_as_sum([5], 10) is False


def test_two_elements_match():
    """Два элемента, сумма которых равна target"""
    assert find_target_as_sum([1, 4], 5) is True


def test_two_elements_no_match():
    """Два элемента, сумма которых не равна target"""
    assert find_target_as_sum([1, 2], 5) is False


def test_multiple_elements_match():
    """Несколько элементов, пара существует"""
    assert find_target_as_sum([1, 2, 3, 4, 5], 9) is True


def test_multiple_elements_no_match():
    """Несколько элементов, пары не существует"""
    assert find_target_as_sum([1, 2, 3, 4, 5], 20) is False


def test_target_is_sum_of_first_two():
    """Target равен сумме первых двух элементов"""
    assert find_target_as_sum([1, 2, 5, 7, 9], 3) is True


def test_target_is_sum_of_last_two():
    """Target равен сумме последних двух элементов"""
    assert find_target_as_sum([1, 2, 5, 7, 9], 16) is True


def test_target_is_sum_of_middle_elements():
    """Target равен сумме средних элементов"""
    assert find_target_as_sum([1, 3, 5, 7, 9], 8) is True


def test_negative_numbers_match():
    """Отрицательные числа, пара существует"""
    assert find_target_as_sum([-5, -3, -1, 0, 2], -4) is True
    assert find_target_as_sum([-5, -3, -1, 2, 4], -2) is False
    assert find_target_as_sum([-5, -3, 1, 2, 4], -4) is True


def test_negative_and_positive_numbers():
    """Смешанные отрицательные и положительные числа"""
    assert find_target_as_sum([-5, -2, 0, 3, 7], 2) is True
    assert find_target_as_sum([-5, -2, 0, 3, 7], 5) is True


def test_all_negative_numbers():
    """Все числа отрицательные"""
    assert find_target_as_sum([-10, -8, -5, -3, -1], -11) is True
    assert find_target_as_sum([-10, -8, -5, -3, -1], -20) is False


def test_all_positive_numbers():
    """Все числа положительные"""
    assert find_target_as_sum([1, 3, 5, 7, 9], 10) is True
    assert find_target_as_sum([1, 3, 5, 7, 9], 100) is False


def test_zero_in_array():
    """Ноль в массиве"""
    assert find_target_as_sum([-5, 0, 5], 0) is True
    assert find_target_as_sum([-5, 0, 5], 5) is True


def test_duplicate_elements_match():
    """Дубликаты элементов, пара существует"""
    assert find_target_as_sum([1, 2, 2, 3, 4], 4) is True


def test_duplicate_elements_no_match():
    """Дубликаты элементов, пары не существует"""
    assert find_target_as_sum([1, 2, 2, 3, 4], 10) is False


def test_large_array_match():
    """Большой массив, пара существует"""
    arr = list(range(1, 101))  # 1 to 100
    assert find_target_as_sum(arr, 101) is True


def test_large_array_no_match():
    """Большой массив, пары не существует"""
    arr = list(range(1, 101))  # 1 to 100
    assert find_target_as_sum(arr, 201) is False


def test_target_less_than_minimum_sum():
    """Target меньше минимально возможной суммы"""
    assert find_target_as_sum([5, 10, 15, 20], 3) is False


def test_target_greater_than_maximum_sum():
    """Target больше максимально возможной суммы"""
    assert find_target_as_sum([5, 10, 15, 20], 100) is False


def test_exact_minimum_sum():
    """Target равен минимально возможной сумме"""
    assert find_target_as_sum([5, 10, 15, 20], 15) is True


def test_exact_maximum_sum():
    """Target равен максимально возможной сумме"""
    assert find_target_as_sum([5, 10, 15, 20], 35) is True


def test_multiple_pairs_exist():
    """Существует несколько пар с одинаковой суммой"""
    assert find_target_as_sum([1, 2, 3, 4, 5, 6], 7) is True


def test_only_one_pair_exists():
    """Существует только одна пара"""
    assert find_target_as_sum([1, 5, 10, 15], 16) is True


def test_consecutive_numbers():
    """Последовательные числа"""
    assert find_target_as_sum([1, 2, 3, 4, 5], 5) is True


def test_even_numbers_only():
    """Только четные числа"""
    assert find_target_as_sum([2, 4, 6, 8, 10], 12) is True
    assert find_target_as_sum([2, 4, 6, 8, 10], 13) is False


def test_odd_numbers_only():
    """Только нечетные числа"""
    assert find_target_as_sum([1, 3, 5, 7, 9], 10) is True
    assert find_target_as_sum([1, 3, 5, 7, 9], 11) is False


def test_target_is_double_of_element():
    """Target равен удвоенному значению элемента (нужны два одинаковых)"""
    assert find_target_as_sum([1, 2, 3, 4, 5], 6) is True
    assert find_target_as_sum([1, 3, 3, 5], 6) is True


def test_array_with_gaps():
    """Массив с большими промежутками между числами"""
    assert find_target_as_sum([1, 10, 50, 100, 500], 51) is True
    assert find_target_as_sum([1, 10, 50, 100, 500], 55) is False


def test_target_zero():
    """Target равен нулю"""
    assert find_target_as_sum([-5, -2, 0, 2, 5], 0) is True
    assert find_target_as_sum([1, 2, 3], 0) is False


def test_very_large_numbers():
    """Очень большие числа"""
    assert find_target_as_sum([1000000, 2000000, 3000000], 3000000) is True
    assert find_target_as_sum([1000000, 2000000, 3000000], 6000000) is False