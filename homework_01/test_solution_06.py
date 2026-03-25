from homework_01.solutions import solution_06


# ==================== Базовые тесты ====================

def test_move_evens_empty_array():
    result = solution_06([])
    assert result == []


def test_move_evens_single_even():
    result = solution_06([2])
    assert result == [2]


def test_move_evens_single_odd():
    result = solution_06([1])
    assert result == [1]


def test_move_evens_two_evens():
    result = solution_06([2, 4])
    assert result == [2, 4]


def test_move_evens_two_odds():
    result = solution_06([1, 3])
    assert result == [1, 3]


# ==================== Два элемента ====================

def test_move_evens_two_elements_ee():
    result = solution_06([2, 4])
    assert result == [2, 4]


def test_move_evens_two_elements_eo():
    result = solution_06([2, 1])
    assert result == [2, 1]


def test_move_evens_two_elements_oe():
    result = solution_06([1, 2])
    assert result == [2, 1]


def test_move_evens_two_elements_oo():
    result = solution_06([1, 3])
    assert result == [1, 3]


# ==================== Три элемента ====================

def test_move_evens_three_eee():
    result = solution_06([2, 4, 6])
    assert result == [2, 4, 6]


def test_move_evens_three_eeo():
    result = solution_06([2, 4, 1])
    assert result == [2, 4, 1]


def test_move_evens_three_eoe():
    result = solution_06([2, 1, 4])
    assert result == [2, 4, 1]


def test_move_evens_three_eoo():
    result = solution_06([2, 1, 3])
    assert result == [2, 1, 3]


def test_move_evens_three_oee():
    result = solution_06([1, 2, 4])
    assert result == [2, 4, 1]


def test_move_evens_three_oeo():
    result = solution_06([1, 2, 3])
    assert result == [2, 1, 3]


def test_move_evens_three_ooe():
    result = solution_06([1, 3, 2])
    assert result == [2, 3, 1]


def test_move_evens_three_ooo():
    result = solution_06([1, 3, 5])
    assert result == [1, 3, 5]


# ==================== Проверка: все четные перед нечетными ====================

def test_move_evens_all_evens_before_odds_1():
    result = solution_06([3, 8, 5, 2, 7, 4])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds
    assert len(evens) == 3
    assert len(odds) == 3


def test_move_evens_all_evens_before_odds_2():
    result = solution_06([1, 2, 3, 4, 5, 6])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_all_evens_before_odds_3():
    result = solution_06([5, 8, 3, 10, 1, 6, 9, 2, 7, 4])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


# ==================== Все четные ====================

def test_move_evens_all_evens_3():
    result = solution_06([2, 4, 6])
    assert all(x % 2 == 0 for x in result)


def test_move_evens_all_evens_5():
    result = solution_06([2, 4, 6, 8, 10])
    assert all(x % 2 == 0 for x in result)


def test_move_evens_all_evens_10():
    result = solution_06([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    assert all(x % 2 == 0 for x in result)


# ==================== Все нечетные ====================

def test_move_evens_all_odds_3():
    result = solution_06([1, 3, 5])
    assert all(x % 2 != 0 for x in result)


def test_move_evens_all_odds_5():
    result = solution_06([1, 3, 5, 7, 9])
    assert all(x % 2 != 0 for x in result)


def test_move_evens_all_odds_10():
    result = solution_06([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
    assert all(x % 2 != 0 for x in result)


# ==================== Четные в начале (уже отсортировано) ====================

def test_move_evens_already_sorted():
    result = solution_06([2, 4, 6, 1, 3, 5])
    assert result[:3] == [2, 4, 6]
    assert result[3:] == [1, 3, 5]


def test_move_evens_already_sorted_2():
    result = solution_06([2, 4, 1, 3])
    assert result[:2] == [2, 4]
    assert result[2:] == [1, 3]


# ==================== Четные в конце ====================

def test_move_evens_evens_at_end():
    result = solution_06([1, 3, 5, 2, 4, 6])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_evens_at_end_2():
    result = solution_06([1, 3, 2, 4])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


# ==================== Чередование ====================

def test_move_evens_alternating_1():
    result = solution_06([1, 2, 3, 4, 5, 6])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_alternating_2():
    result = solution_06([2, 1, 4, 3, 6, 5])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_alternating_3():
    result = solution_06([1, 2, 1, 2, 1, 2])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


# ==================== Отрицательные числа ====================

def test_move_evens_negative_evens():
    result = solution_06([-2, -4, -6])
    assert all(x % 2 == 0 for x in result)


def test_move_evens_negative_mixed():
    result = solution_06([-2, 1, -4, 3, -6])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_negative_and_positive():
    result = solution_06([-1, 2, -3, 4, -5, 6])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_zero_is_even():
    result = solution_06([1, 0, 3, 2, 5])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds
    assert 0 in evens


def test_move_evens_multiple_zeros():
    result = solution_06([0, 1, 0, 3, 0, 5])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds
    assert evens.count(0) == 3


# ==================== Большие массивы ====================

def test_move_evens_large_20():
    result = solution_06(list(range(1, 21)))
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds
    assert len(evens) == 10
    assert len(odds) == 10


def test_move_evens_large_reverse():
    result = solution_06(list(range(20, 0, -1)))
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_large_random():
    result = solution_06([5, 8, 3, 10, 1, 6, 9, 2, 7, 4])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


# ==================== Граничные значения ====================

def test_move_evens_with_max_int():
    result = solution_06([1, 2147483646, 3, 2147483647])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_with_min_int():
    result = solution_06([-2147483648, 1, -2147483647, 2])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_with_zero():
    result = solution_06([0, 1, 2, 3, 4])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


# ==================== Специфические паттерны ====================

def test_move_evens_pattern_1():
    result = solution_06([1, 1, 1, 2, 2, 2])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_pattern_2():
    result = solution_06([2, 2, 2, 1, 1, 1])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_pattern_3():
    result = solution_06([1, 2, 2, 1, 2, 1])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_pattern_4():
    result = solution_06([2, 1, 1, 2, 1, 2])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


# ==================== Проверка in-place ====================

def test_move_evens_modifies_original():
    arr = [1, 2, 3, 4]
    original_id = id(arr)
    result = solution_06(arr)
    assert id(result) == original_id


def test_move_evens_returns_same_object():
    arr = [1, 2, 3]
    result = solution_06(arr)
    assert result is arr


# ==================== Универсальная проверка ====================

def test_move_evens_universal_check_1():
    """Универсальный тест: проверяем что все четные перед нечетными"""
    arr = [3, 8, 5, 2, 7, 4]
    result = solution_06(arr.copy())
    
    # Находим границу между четными и нечетными
    first_odd_index = None
    for i, num in enumerate(result):
        if num % 2 != 0:
            first_odd_index = i
            break
    
    # Если есть нечетные, проверяем что после них нет четных
    if first_odd_index is not None:
        for i in range(first_odd_index, len(result)):
            assert result[i] % 2 != 0, f"Нечетное число должно быть после позиции {first_odd_index}"
    
    # Проверяем количество четных
    assert sum(1 for x in result if x % 2 == 0) == sum(1 for x in arr if x % 2 == 0)


def test_move_evens_universal_check_2():
    arr = [1, 10, 3, 8, 5, 6, 7, 4]
    result = solution_06(arr.copy())
    
    first_odd_index = None
    for i, num in enumerate(result):
        if num % 2 != 0:
            first_odd_index = i
            break
    
    if first_odd_index is not None:
        for i in range(first_odd_index, len(result)):
            assert result[i] % 2 != 0
    
    assert sum(1 for x in result if x % 2 == 0) == sum(1 for x in arr if x % 2 == 0)


def test_move_evens_universal_check_3():
    arr = [7, 2, 9, 4, 1, 6, 3, 8]
    result = solution_06(arr.copy())
    
    first_odd_index = None
    for i, num in enumerate(result):
        if num % 2 != 0:
            first_odd_index = i
            break
    
    if first_odd_index is not None:
        for i in range(first_odd_index, len(result)):
            assert result[i] % 2 != 0
    
    assert sum(1 for x in result if x % 2 == 0) == sum(1 for x in arr if x % 2 == 0)


# ==================== Случайные тесты ====================

def test_move_evens_random_1():
    result = solution_06([5, 2, 9, 4, 7, 6, 1, 8])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_random_2():
    result = solution_06([10, 3, 7, 8, 5, 2, 9, 4])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_random_3():
    result = solution_06([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_random_4():
    result = solution_06([12, 1, 14, 3, 16, 5, 18, 7])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds


def test_move_evens_random_5():
    result = solution_06([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    evens = [x for x in result if x % 2 == 0]
    odds = [x for x in result if x % 2 != 0]
    assert result == evens + odds