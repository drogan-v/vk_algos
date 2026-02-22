from homework_01.solutions import solution_03
import pytest


# ==================== Базовые тесты ====================

def test_merge_inplace_both_empty():
    arr1 = []
    arr2 = []
    result = solution_03(arr1, arr2)
    assert result == []


def test_merge_inplace_first_empty():
    arr1 = [0, 0, 0]
    arr2 = [1, 2, 3]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3]


def test_merge_inplace_second_empty():
    arr1 = [1, 2, 3]
    arr2 = []
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3]


def test_merge_inplace_single_elements():
    arr1 = [1, 0]
    arr2 = [2]
    result = solution_03(arr1, arr2)
    assert result == [1, 2]


def test_merge_inplace_single_elements_reverse():
    arr1 = [2, 0]
    arr2 = [1]
    result = solution_03(arr1, arr2)
    assert result == [1, 2]


# ==================== Одинаковый размер массивов ====================

def test_merge_inplace_equal_size_2():
    arr1 = [1, 3, 0, 0]
    arr2 = [2, 4]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4]


def test_merge_inplace_equal_size_3():
    arr1 = [1, 3, 5, 0, 0, 0]
    arr2 = [2, 4, 6]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_inplace_equal_size_4():
    arr1 = [1, 3, 5, 7, 0, 0, 0, 0]
    arr2 = [2, 4, 6, 8]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


# ==================== Разный размер массивов ====================

def test_merge_inplace_first_smaller():
    arr1 = [1, 2, 0, 0, 0, 0, 0]
    arr2 = [3, 4, 5, 6, 7]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7]


def test_merge_inplace_first_larger():
    arr1 = [1, 2, 3, 4, 5, 0, 0]
    arr2 = [6, 7]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7]


def test_merge_inplace_first_much_smaller():
    arr1 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_inplace_first_much_larger():
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    arr2 = [10]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==================== Все элементы одинаковые ====================

def test_merge_inplace_all_same_first():
    arr1 = [5, 5, 5, 0, 0, 0]
    arr2 = [1, 1, 1]
    result = solution_03(arr1, arr2)
    assert result == [1, 1, 1, 5, 5, 5]


def test_merge_inplace_all_same_second():
    arr1 = [1, 1, 1, 0, 0, 0]
    arr2 = [5, 5, 5]
    result = solution_03(arr1, arr2)
    assert result == [1, 1, 1, 5, 5, 5]


def test_merge_inplace_all_same_both():
    arr1 = [3, 3, 3, 0, 0, 0]
    arr2 = [3, 3, 3]
    result = solution_03(arr1, arr2)
    assert result == [3, 3, 3, 3, 3, 3]


# ==================== Дубликаты ====================

def test_merge_inplace_with_duplicates_1():
    arr1 = [1, 2, 2, 3, 0, 0, 0]
    arr2 = [2, 3, 4]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 2, 2, 3, 3, 4]


def test_merge_inplace_with_duplicates_2():
    arr1 = [1, 1, 1, 0, 0, 0]
    arr2 = [1, 1, 1]
    result = solution_03(arr1, arr2)
    assert result == [1, 1, 1, 1, 1, 1]


def test_merge_inplace_with_duplicates_3():
    arr1 = [1, 3, 3, 5, 0, 0, 0, 0]
    arr2 = [2, 3, 3, 6]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 3, 3, 3, 5, 6]


def test_merge_inplace_with_duplicates_4():
    arr1 = [1, 1, 2, 2, 0, 0, 0, 0]
    arr2 = [1, 2, 2, 3]
    result = solution_03(arr1, arr2)
    assert result == [1, 1, 1, 2, 2, 2, 2, 3]


# ==================== Отрицательные числа ====================

def test_merge_inplace_negative_numbers():
    arr1 = [-5, -3, -1, 0, 0, 0]
    arr2 = [-4, -2, 0]
    result = solution_03(arr1, arr2)
    assert result == [-5, -4, -3, -2, -1, 0]


def test_merge_inplace_mixed_positive_negative():
    arr1 = [-3, -1, 0, 0, 0, 0]
    arr2 = [1, 2, 3]
    result = solution_03(arr1, arr2)
    assert result == [-3, -1, 0, 1, 2, 3]


def test_merge_inplace_all_negative():
    arr1 = [-5, -3, -1, 0, 0, 0]
    arr2 = [-4, -2, -1]
    result = solution_03(arr1, arr2)
    assert result == [-5, -4, -3, -2, -1, -1]


def test_merge_inplace_negative_and_positive():
    arr1 = [-10, -5, 0, 0, 0, 0]
    arr2 = [5, 10, 15]
    result = solution_03(arr1, arr2)
    assert result == [-10, -5, 0, 5, 10, 15]


# ==================== Один элемент в одном массиве ====================

def test_merge_inplace_one_in_first():
    arr1 = [5, 0, 0, 0, 0, 0, 0, 0]
    arr2 = [1, 2, 3, 4, 6, 7, 8]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_inplace_one_in_second():
    arr1 = [1, 2, 3, 4, 6, 7, 8, 0]
    arr2 = [5]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_inplace_one_in_first_beginning():
    arr1 = [1, 0, 0, 0, 0]
    arr2 = [2, 3, 4, 5]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5]


def test_merge_inplace_one_in_first_end():
    arr1 = [10, 0, 0, 0, 0]
    arr2 = [1, 2, 3, 4]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 10]


def test_merge_inplace_one_in_second_beginning():
    arr1 = [2, 3, 4, 5, 0]
    arr2 = [1]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5]


def test_merge_inplace_one_in_second_end():
    arr1 = [1, 2, 3, 4, 0]
    arr2 = [5]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5]


# ==================== Чередование элементов ====================

def test_merge_inplace_alternating():
    arr1 = [1, 3, 5, 7, 0, 0, 0, 0]
    arr2 = [2, 4, 6, 8]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_inplace_alternating_reverse():
    arr1 = [2, 4, 6, 8, 0, 0, 0, 0]
    arr2 = [1, 3, 5, 7]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_inplace_alternating_odd():
    arr1 = [1, 3, 5, 0, 0, 0]
    arr2 = [2, 4, 6]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]


# ==================== Один массив полностью меньше другого ====================

def test_merge_inplace_first_all_smaller():
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [4, 5, 6]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_inplace_first_all_larger():
    arr1 = [4, 5, 6, 0, 0, 0]
    arr2 = [1, 2, 3]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_inplace_first_all_smaller_large():
    arr1 = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
    arr2 = [6, 7, 8, 9, 10]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_inplace_first_all_larger_large():
    arr1 = [6, 7, 8, 9, 10, 0, 0, 0, 0, 0]
    arr2 = [1, 2, 3, 4, 5]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==================== Большие массивы ====================

def test_merge_inplace_large_arrays():
    arr1 = list(range(0, 100, 2)) + [0] * 50
    arr2 = list(range(1, 100, 2))
    result = solution_03(arr1, arr2)
    assert result == list(range(100))


def test_merge_inplace_large_arrays_reverse():
    arr1 = list(range(1, 100, 2)) + [0] * 50
    arr2 = list(range(0, 100, 2))
    result = solution_03(arr1, arr2)
    assert result == list(range(100))


def test_merge_inplace_large_same_size():
    arr1 = list(range(0, 50)) + [0] * 50
    arr2 = list(range(50, 100))
    result = solution_03(arr1, arr2)
    assert result == list(range(100))


# ==================== Граничные значения ====================

def test_merge_inplace_with_zero():
    arr1 = [-2, -1, 0, 0, 0, 0]
    arr2 = [0, 1, 2]
    result = solution_03(arr1, arr2)
    assert result == [-2, -1, 0, 0, 1, 2]


def test_merge_inplace_with_max_int():
    arr1 = [1, 2, 3, 0]
    arr2 = [2147483647]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 2147483647]


def test_merge_inplace_with_min_int():
    arr1 = [-2147483648, 0, 0, 0]
    arr2 = [1, 2, 3]
    result = solution_03(arr1, arr2)
    assert result == [-2147483648, 1, 2, 3]


# ==================== Специфические паттерны ====================

def test_merge_inplace_interleaved_1():
    arr1 = [1, 5, 9, 0, 0, 0]
    arr2 = [2, 6, 10]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 5, 6, 9, 10]


def test_merge_inplace_interleaved_2():
    arr1 = [1, 10, 20, 0, 0, 0]
    arr2 = [5, 15, 25]
    result = solution_03(arr1, arr2)
    assert result == [1, 5, 10, 15, 20, 25]


def test_merge_inplace_close_values():
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [1, 2, 3]
    result = solution_03(arr1, arr2)
    assert result == [1, 1, 2, 2, 3, 3]


def test_merge_inplace_overlapping_ranges():
    arr1 = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
    arr2 = [3, 4, 5, 6, 7]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]


# ==================== Классические примеры (LeetCode 88) ====================

def test_merge_inplace_leetcode_example1():
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 2, 3, 5, 6]


def test_merge_inplace_leetcode_example2():
    arr1 = [1]
    arr2 = []
    result = solution_03(arr1, arr2)
    assert result == [1]


def test_merge_inplace_leetcode_example3():
    arr1 = [0]
    arr2 = [1]
    result = solution_03(arr1, arr2)
    assert result == [1]


# ==================== Случайные тесты ====================

def test_merge_inplace_random_1():
    arr1 = [1, 5, 8, 10, 0, 0, 0, 0]
    arr2 = [2, 3, 7, 9]
    result = solution_03(arr1, arr2)
    assert result == [1, 2, 3, 5, 7, 8, 9, 10]


def test_merge_inplace_random_2():
    arr1 = [0, 2, 4, 6, 0, 0, 0, 0]
    arr2 = [1, 3, 5, 7]
    result = solution_03(arr1, arr2)
    assert result == [0, 1, 2, 3, 4, 5, 6, 7]


def test_merge_inplace_random_3():
    arr1 = [10, 20, 30, 0, 0, 0]
    arr2 = [15, 25, 35]
    result = solution_03(arr1, arr2)
    assert result == [10, 15, 20, 25, 30, 35]


def test_merge_inplace_random_4():
    arr1 = [-5, 0, 5, 0, 0, 0]
    arr2 = [-3, 2, 7]
    result = solution_03(arr1, arr2)
    assert result == [-5, -3, 0, 2, 5, 7]


def test_merge_inplace_random_5():
    arr1 = [1, 1, 3, 3, 0, 0, 0, 0]
    arr2 = [2, 2, 4, 4]
    result = solution_03(arr1, arr2)
    assert result == [1, 1, 2, 2, 3, 3, 4, 4]


# ==================== Проверка что массив меняется in-place ====================

def test_merge_inplace_modifies_original():
    arr1 = [1, 3, 5, 0, 0, 0]
    arr2 = [2, 4, 6]
    original_id = id(arr1)
    result = solution_03(arr1, arr2)
    assert id(result) == original_id  # Тот же объект
    assert arr1 == [1, 2, 3, 4, 5, 6]


def test_merge_inplace_returns_same_object():
    arr1 = [1, 2, 0]
    arr2 = [3]
    result = solution_03(arr1, arr2)
    assert result is arr1