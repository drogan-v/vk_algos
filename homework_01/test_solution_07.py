from homework_01.solutions import solution_07
import pytest


# ==================== Базовые тесты ====================

def test_move_zeroes_empty_array():
    result = solution_07([])
    assert result == []


def test_move_zeroes_single_zero():
    result = solution_07([0])
    assert result == [0]


def test_move_zeroes_single_nonzero():
    result = solution_07([5])
    assert result == [5]


def test_move_zeroes_two_zeros():
    result = solution_07([0, 0])
    assert result == [0, 0]


def test_move_zeroes_two_nonzeros():
    result = solution_07([1, 2])
    assert result == [1, 2]


# ==================== Два элемента ====================

def test_move_zeroes_two_00():
    result = solution_07([0, 0])
    assert result == [0, 0]


def test_move_zeroes_two_01():
    result = solution_07([0, 1])
    assert result == [1, 0]


def test_move_zeroes_two_10():
    result = solution_07([1, 0])
    assert result == [1, 0]


def test_move_zeroes_two_12():
    result = solution_07([1, 2])
    assert result == [1, 2]


# ==================== Три элемента ====================

def test_move_zeroes_three_000():
    result = solution_07([0, 0, 0])
    assert result == [0, 0, 0]


def test_move_zeroes_three_001():
    result = solution_07([0, 0, 1])
    assert result == [1, 0, 0]


def test_move_zeroes_three_010():
    result = solution_07([0, 1, 0])
    assert result == [1, 0, 0]


def test_move_zeroes_three_012():
    result = solution_07([0, 1, 2])
    assert result == [1, 2, 0]


def test_move_zeroes_three_100():
    result = solution_07([1, 0, 0])
    assert result == [1, 0, 0]


def test_move_zeroes_three_101():
    result = solution_07([1, 0, 1])
    assert result == [1, 1, 0]


def test_move_zeroes_three_102():
    result = solution_07([1, 0, 2])
    assert result == [1, 2, 0]


def test_move_zeroes_three_120():
    result = solution_07([1, 2, 0])
    assert result == [1, 2, 0]


def test_move_zeroes_three_123():
    result = solution_07([1, 2, 3])
    assert result == [1, 2, 3]


# ==================== Классические примеры (LeetCode 283) ====================

def test_move_zeroes_leetcode_example1():
    result = solution_07([0, 1, 0, 3, 12])
    assert result == [1, 3, 12, 0, 0]


def test_move_zeroes_leetcode_example2():
    result = solution_07([0])
    assert result == [0]


# ==================== Сохранение порядка ненулевых ====================

def test_move_zeroes_preserve_order_1():
    """Проверяем что порядок ненулевых элементов сохранён"""
    result = solution_07([0, 1, 0, 3, 12])
    nonzeros = [x for x in result if x != 0]
    assert nonzeros == [1, 3, 12]


def test_move_zeroes_preserve_order_2():
    result = solution_07([4, 2, 0, 1, 0, 3])
    nonzeros = [x for x in result if x != 0]
    assert nonzeros == [4, 2, 1, 3]


def test_move_zeroes_preserve_order_3():
    result = solution_07([5, 0, 3, 0, 1, 0, 2])
    nonzeros = [x for x in result if x != 0]
    assert nonzeros == [5, 3, 1, 2]


def test_move_zeroes_preserve_order_4():
    result = solution_07([1, 2, 3, 0, 0, 0])
    nonzeros = [x for x in result if x != 0]
    assert nonzeros == [1, 2, 3]


def test_move_zeroes_preserve_order_5():
    result = solution_07([0, 0, 0, 1, 2, 3])
    nonzeros = [x for x in result if x != 0]
    assert nonzeros == [1, 2, 3]


# ==================== Все нули ====================

def test_move_zeroes_all_zeros_3():
    result = solution_07([0, 0, 0])
    assert result == [0, 0, 0]


def test_move_zeroes_all_zeros_5():
    result = solution_07([0, 0, 0, 0, 0])
    assert result == [0, 0, 0, 0, 0]


def test_move_zeroes_all_zeros_10():
    result = solution_07([0] * 10)
    assert result == [0] * 10


# ==================== Нет нулей ====================

def test_move_zeroes_no_zeros_3():
    result = solution_07([1, 2, 3])
    assert result == [1, 2, 3]


def test_move_zeroes_no_zeros_5():
    result = solution_07([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_move_zeroes_no_zeros_10():
    result = solution_07(list(range(1, 11)))
    assert result == list(range(1, 11))


# ==================== Нули в начале ====================

def test_move_zeroes_zeros_at_start_1():
    result = solution_07([0, 1, 2, 3])
    assert result == [1, 2, 3, 0]


def test_move_zeroes_zeros_at_start_2():
    result = solution_07([0, 0, 1, 2, 3])
    assert result == [1, 2, 3, 0, 0]


def test_move_zeroes_zeros_at_start_3():
    result = solution_07([0, 0, 0, 1, 2])
    assert result == [1, 2, 0, 0, 0]


# ==================== Нули в конце ====================

def test_move_zeroes_zeros_at_end_1():
    result = solution_07([1, 2, 3, 0])
    assert result == [1, 2, 3, 0]


def test_move_zeroes_zeros_at_end_2():
    result = solution_07([1, 2, 3, 0, 0])
    assert result == [1, 2, 3, 0, 0]


def test_move_zeroes_zeros_at_end_3():
    result = solution_07([1, 2, 0, 0, 0])
    assert result == [1, 2, 0, 0, 0]


# ==================== Нули посередине ====================

def test_move_zeroes_zeros_in_middle_1():
    result = solution_07([1, 0, 2, 3, 4])
    assert result == [1, 2, 3, 4, 0]


def test_move_zeroes_zeros_in_middle_2():
    result = solution_07([1, 2, 0, 0, 3, 4])
    assert result == [1, 2, 3, 4, 0, 0]


def test_move_zeroes_zeros_in_middle_3():
    result = solution_07([1, 2, 3, 0, 0, 4, 5])
    assert result == [1, 2, 3, 4, 5, 0, 0]


# ==================== Чередование ====================

def test_move_zeroes_alternating_1():
    result = solution_07([0, 1, 0, 2, 0, 3])
    assert result == [1, 2, 3, 0, 0, 0]


def test_move_zeroes_alternating_2():
    result = solution_07([1, 0, 2, 0, 3, 0])
    assert result == [1, 2, 3, 0, 0, 0]


def test_move_zeroes_alternating_3():
    result = solution_07([0, 1, 0, 1, 0, 1])
    assert result == [1, 1, 1, 0, 0, 0]


# ==================== Отрицательные числа ====================

def test_move_zeroes_negative_numbers():
    result = solution_07([-1, -2, 0, -3, 0, -4])
    assert result == [-1, -2, -3, -4, 0, 0]


def test_move_zeroes_mixed_positive_negative():
    result = solution_07([1, 0, -2, 0, 3, 0, -4])
    assert result == [1, -2, 3, -4, 0, 0, 0]


def test_move_zeroes_with_zero_value():
    result = solution_07([0, 1, 0, -1, 0, 2])
    assert result == [1, -1, 2, 0, 0, 0]


# ==================== Большие массивы ====================

def test_move_zeroes_large_20():
    result = solution_07([0, 1, 0, 2, 0, 3, 0, 4, 0, 5,
                          0, 6, 0, 7, 0, 8, 0, 9, 0, 10])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_move_zeroes_large_50():
    arr = [0 if i % 2 == 0 else i for i in range(1, 51)]
    result = solution_07(arr)
    nonzeros = [x for x in result if x != 0]
    zeros_count = result.count(0)
    assert len(nonzeros) == 25
    assert zeros_count == 25
    assert nonzeros == list(range(1, 51, 2))


def test_move_zeroes_large_100():
    arr = list(range(1, 101)) + [0] * 50
    result = solution_07(arr)
    nonzeros = [x for x in result if x != 0]
    assert nonzeros == list(range(1, 101))
    assert result.count(0) == 50


# ==================== Граничные значения ====================

def test_move_zeroes_with_max_int():
    result = solution_07([0, 2147483647, 0, 1])
    assert result == [2147483647, 1, 0, 0]


def test_move_zeroes_with_min_int():
    result = solution_07([-2147483648, 0, 1, 0])
    assert result == [-2147483648, 1, 0, 0]


def test_move_zeroes_multiple_zeros():
    result = solution_07([0, 0, 0, 0, 1])
    assert result == [1, 0, 0, 0, 0]


# ==================== Специфические паттерны ====================

def test_move_zeroes_pattern_1():
    result = solution_07([1, 0, 1, 0, 1, 0, 1])
    assert result == [1, 1, 1, 1, 0, 0, 0]


def test_move_zeroes_pattern_2():
    result = solution_07([0, 1, 1, 0, 1, 1, 0])
    assert result == [1, 1, 1, 1, 0, 0, 0]


def test_move_zeroes_pattern_3():
    result = solution_07([1, 1, 1, 0, 0, 0, 0])
    assert result == [1, 1, 1, 0, 0, 0, 0]


def test_move_zeroes_pattern_4():
    result = solution_07([0, 0, 0, 0, 1, 1, 1])
    assert result == [1, 1, 1, 0, 0, 0, 0]


# ==================== Проверка in-place ====================

def test_move_zeroes_modifies_original():
    arr = [0, 1, 0, 3, 12]
    original_id = id(arr)
    result = solution_07(arr)
    assert id(result) == original_id
    assert arr == [1, 3, 12, 0, 0]


def test_move_zeroes_returns_same_object():
    arr = [1, 0, 2]
    result = solution_07(arr)
    assert result is arr


# ==================== Универсальная проверка ====================

def test_move_zeroes_universal_check_1():
    """Проверяем что все нули в конце, порядок ненулевых сохранён"""
    arr = [0, 1, 0, 3, 12]
    result = solution_07(arr.copy())
    
    # Находим первый ноль
    first_zero_index = None
    for i, num in enumerate(result):
        if num == 0:
            first_zero_index = i
            break
    
    # Если есть нули, проверяем что после них нет ненулевых
    if first_zero_index is not None:
        for i in range(first_zero_index, len(result)):
            assert result[i] == 0
    
    # Проверяем количество нулей
    assert result.count(0) == arr.count(0)
    
    # Проверяем порядок ненулевых
    nonzeros_result = [x for x in result if x != 0]
    nonzeros_original = [x for x in arr if x != 0]
    assert nonzeros_result == nonzeros_original


def test_move_zeroes_universal_check_2():
    arr = [4, 2, 0, 1, 0, 3]
    result = solution_07(arr.copy())
    
    first_zero_index = None
    for i, num in enumerate(result):
        if num == 0:
            first_zero_index = i
            break
    
    if first_zero_index is not None:
        for i in range(first_zero_index, len(result)):
            assert result[i] == 0
    
    assert result.count(0) == arr.count(0)
    
    nonzeros_result = [x for x in result if x != 0]
    nonzeros_original = [x for x in arr if x != 0]
    assert nonzeros_result == nonzeros_original


def test_move_zeroes_universal_check_3():
    arr = [5, 0, 3, 0, 1, 0, 2]
    result = solution_07(arr.copy())
    
    first_zero_index = None
    for i, num in enumerate(result):
        if num == 0:
            first_zero_index = i
            break
    
    if first_zero_index is not None:
        for i in range(first_zero_index, len(result)):
            assert result[i] == 0
    
    assert result.count(0) == arr.count(0)
    
    nonzeros_result = [x for x in result if x != 0]
    nonzeros_original = [x for x in arr if x != 0]
    assert nonzeros_result == nonzeros_original


# ==================== Случайные тесты ====================

def test_move_zeroes_random_1():
    result = solution_07([5, 0, 9, 0, 7, 0, 1])
    assert result == [5, 9, 7, 1, 0, 0, 0]


def test_move_zeroes_random_2():
    result = solution_07([0, 8, 0, 6, 0, 4, 0, 2])
    assert result == [8, 6, 4, 2, 0, 0, 0, 0]


def test_move_zeroes_random_3():
    result = solution_07([3, 0, 0, 0, 0, 0, 0, 1])
    assert result == [3, 1, 0, 0, 0, 0, 0, 0]


def test_move_zeroes_random_4():
    result = solution_07([0, 0, 0, 1, 0, 0, 2, 0])
    assert result == [1, 2, 0, 0, 0, 0, 0, 0]


def test_move_zeroes_random_5():
    result = solution_07([1, 2, 3, 0, 4, 0, 5, 0, 6])
    assert result == [1, 2, 3, 4, 5, 6, 0, 0, 0]