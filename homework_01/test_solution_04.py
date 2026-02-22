from homework_01.solutions import solution_04
import pytest


# ==================== Базовые тесты ====================

def test_sort_01_empty_array():
    result = solution_04([])
    assert result == []


def test_sort_01_single_zero():
    result = solution_04([0])
    assert result == [0]


def test_sort_01_single_one():
    result = solution_04([1])
    assert result == [1]


def test_sort_01_two_zeros():
    result = solution_04([0, 0])
    assert result == [0, 0]


def test_sort_01_two_ones():
    result = solution_04([1, 1])
    assert result == [1, 1]


# ==================== Два элемента ====================

def test_sort_01_two_elements_00():
    result = solution_04([0, 0])
    assert result == [0, 0]


def test_sort_01_two_elements_01():
    result = solution_04([0, 1])
    assert result == [0, 1]


def test_sort_01_two_elements_10():
    result = solution_04([1, 0])
    assert result == [0, 1]


def test_sort_01_two_elements_11():
    result = solution_04([1, 1])
    assert result == [1, 1]


# ==================== Три элемента ====================

def test_sort_01_three_elements_000():
    result = solution_04([0, 0, 0])
    assert result == [0, 0, 0]


def test_sort_01_three_elements_001():
    result = solution_04([0, 0, 1])
    assert result == [0, 0, 1]


def test_sort_01_three_elements_010():
    result = solution_04([0, 1, 0])
    assert result == [0, 0, 1]


def test_sort_01_three_elements_011():
    result = solution_04([0, 1, 1])
    assert result == [0, 1, 1]


def test_sort_01_three_elements_100():
    result = solution_04([1, 0, 0])
    assert result == [0, 0, 1]


def test_sort_01_three_elements_101():
    result = solution_04([1, 0, 1])
    assert result == [0, 1, 1]


def test_sort_01_three_elements_110():
    result = solution_04([1, 1, 0])
    assert result == [0, 1, 1]


def test_sort_01_three_elements_111():
    result = solution_04([1, 1, 1])
    assert result == [1, 1, 1]


# ==================== Четыре элемента ====================

def test_sort_01_four_elements_0000():
    result = solution_04([0, 0, 0, 0])
    assert result == [0, 0, 0, 0]


def test_sort_01_four_elements_0001():
    result = solution_04([0, 0, 0, 1])
    assert result == [0, 0, 0, 1]


def test_sort_01_four_elements_0011():
    result = solution_04([0, 0, 1, 1])
    assert result == [0, 0, 1, 1]


def test_sort_01_four_elements_0111():
    result = solution_04([0, 1, 1, 1])
    assert result == [0, 1, 1, 1]


def test_sort_01_four_elements_1111():
    result = solution_04([1, 1, 1, 1])
    assert result == [1, 1, 1, 1]


def test_sort_01_four_elements_1110():
    result = solution_04([1, 1, 1, 0])
    assert result == [0, 1, 1, 1]


def test_sort_01_four_elements_1100():
    result = solution_04([1, 1, 0, 0])
    assert result == [0, 0, 1, 1]


def test_sort_01_four_elements_1000():
    result = solution_04([1, 0, 0, 0])
    assert result == [0, 0, 0, 1]


def test_sort_01_four_elements_alternating():
    result = solution_04([1, 0, 1, 0])
    assert result == [0, 0, 1, 1]


# ==================== Пять элементов ====================

def test_sort_01_five_elements_all_zeros():
    result = solution_04([0, 0, 0, 0, 0])
    assert result == [0, 0, 0, 0, 0]


def test_sort_01_five_elements_all_ones():
    result = solution_04([1, 1, 1, 1, 1])
    assert result == [1, 1, 1, 1, 1]


def test_sort_01_five_elements_mixed_1():
    result = solution_04([1, 0, 1, 0, 1])
    assert result == [0, 0, 1, 1, 1]


def test_sort_01_five_elements_mixed_2():
    result = solution_04([0, 1, 0, 1, 0])
    assert result == [0, 0, 0, 1, 1]


def test_sort_01_five_elements_mixed_3():
    result = solution_04([1, 1, 0, 0, 1])
    assert result == [0, 0, 1, 1, 1]


def test_sort_01_five_elements_reverse_sorted():
    result = solution_04([1, 1, 1, 0, 0])
    assert result == [0, 0, 1, 1, 1]


# ==================== Все нули ====================

def test_sort_01_all_zeros_5():
    result = solution_04([0, 0, 0, 0, 0])
    assert result == [0, 0, 0, 0, 0]


def test_sort_01_all_zeros_10():
    result = solution_04([0] * 10)
    assert result == [0] * 10


def test_sort_01_all_zeros_20():
    result = solution_04([0] * 20)
    assert result == [0] * 20


# ==================== Все единицы ====================

def test_sort_01_all_ones_5():
    result = solution_04([1, 1, 1, 1, 1])
    assert result == [1, 1, 1, 1, 1]


def test_sort_01_all_ones_10():
    result = solution_04([1] * 10)
    assert result == [1] * 10


def test_sort_01_all_ones_20():
    result = solution_04([1] * 20)
    assert result == [1] * 20


# ==================== Уже отсортированные ====================

def test_sort_01_already_sorted():
    result = solution_04([0, 0, 0, 1, 1, 1])
    assert result == [0, 0, 0, 1, 1, 1]


def test_sort_01_already_sorted_small():
    result = solution_04([0, 1])
    assert result == [0, 1]


def test_sort_01_already_sorted_single_zero():
    result = solution_04([0, 0, 1])
    assert result == [0, 0, 1]


def test_sort_01_already_sorted_single_one():
    result = solution_04([0, 1, 1])
    assert result == [0, 1, 1]


# ==================== Обратно отсортированные ====================

def test_sort_01_reverse_sorted():
    result = solution_04([1, 1, 1, 0, 0, 0])
    assert result == [0, 0, 0, 1, 1, 1]


def test_sort_01_reverse_sorted_small():
    result = solution_04([1, 0])
    assert result == [0, 1]


def test_sort_01_reverse_sorted_single_zero():
    result = solution_04([1, 0, 0])
    assert result == [0, 0, 1]


def test_sort_01_reverse_sorted_single_one():
    result = solution_04([1, 1, 0])
    assert result == [0, 1, 1]


# ==================== Чередование ====================

def test_sort_01_alternating_start_0():
    result = solution_04([0, 1, 0, 1, 0, 1])
    assert result == [0, 0, 0, 1, 1, 1]


def test_sort_01_alternating_start_1():
    result = solution_04([1, 0, 1, 0, 1, 0])
    assert result == [0, 0, 0, 1, 1, 1]


def test_sort_01_alternating_even():
    result = solution_04([0, 1, 0, 1])
    assert result == [0, 0, 1, 1]


def test_sort_01_alternating_odd():
    result = solution_04([1, 0, 1, 0, 1])
    assert result == [0, 0, 1, 1, 1]


# ==================== Большие массивы ====================

def test_sort_01_large_array_50():
    arr = [1] * 25 + [0] * 25
    result = solution_04(arr)
    assert result == [0] * 25 + [1] * 25


def test_sort_01_large_array_100():
    arr = [1, 0] * 50
    result = solution_04(arr)
    assert result == [0] * 50 + [1] * 50


def test_sort_01_large_array_mixed():
    arr = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0] * 10
    result = solution_04(arr)
    assert result == [0] * 50 + [1] * 50


# ==================== Один ноль/одна единица ====================

def test_sort_01_single_zero_many_ones():
    result = solution_04([1, 1, 1, 0, 1, 1])
    assert result == [0, 1, 1, 1, 1, 1]


def test_sort_01_single_one_many_zeros():
    result = solution_04([0, 0, 0, 1, 0, 0])
    assert result == [0, 0, 0, 0, 0, 1]


def test_sort_01_zero_at_start():
    result = solution_04([0, 1, 1, 1, 1])
    assert result == [0, 1, 1, 1, 1]


def test_sort_01_zero_at_end():
    result = solution_04([1, 1, 1, 1, 0])
    assert result == [0, 1, 1, 1, 1]


def test_sort_01_one_at_start():
    result = solution_04([1, 0, 0, 0, 0])
    assert result == [0, 0, 0, 0, 1]


def test_sort_01_one_at_end():
    result = solution_04([0, 0, 0, 0, 1])
    assert result == [0, 0, 0, 0, 1]


# ==================== Специфические паттерны ====================

def test_sort_01_pattern_1():
    result = solution_04([1, 0, 0, 1, 1, 0, 1, 0])
    assert result == [0, 0, 0, 0, 1, 1, 1, 1]


def test_sort_01_pattern_2():
    result = solution_04([0, 1, 1, 0, 0, 1, 0, 1])
    assert result == [0, 0, 0, 0, 1, 1, 1, 1]


def test_sort_01_pattern_3():
    result = solution_04([1, 1, 0, 0, 1, 1, 0, 0])
    assert result == [0, 0, 0, 0, 1, 1, 1, 1]


def test_sort_01_pattern_4():
    result = solution_04([0, 0, 1, 1, 0, 0, 1, 1])
    assert result == [0, 0, 0, 0, 1, 1, 1, 1]


# ==================== Граничные случаи ====================

def test_sort_01_zeros_then_ones():
    result = solution_04([0, 0, 0, 1, 1, 1])
    assert result == [0, 0, 0, 1, 1, 1]


def test_sort_01_ones_then_zeros():
    result = solution_04([1, 1, 1, 0, 0, 0])
    assert result == [0, 0, 0, 1, 1, 1]


def test_sort_01_single_zero_middle():
    result = solution_04([1, 1, 0, 1, 1])
    assert result == [0, 1, 1, 1, 1]


def test_sort_01_single_one_middle():
    result = solution_04([0, 0, 1, 0, 0])
    assert result == [0, 0, 0, 0, 1]


# ==================== Проверка in-place ====================

def test_sort_01_modifies_original():
    arr = [1, 0, 1, 0]
    original_id = id(arr)
    result = solution_04(arr)
    assert id(result) == original_id
    assert arr == [0, 0, 1, 1]


def test_sort_01_returns_same_object():
    arr = [1, 0, 1]
    result = solution_04(arr)
    assert result is arr


# ==================== Случайные тесты ====================

def test_sort_01_random_1():
    result = solution_04([1, 0, 1, 1, 0, 0, 1, 0])
    assert result == [0, 0, 0, 0, 1, 1, 1, 1]


def test_sort_01_random_2():
    result = solution_04([0, 1, 0, 0, 1, 1, 0, 1])
    assert result == [0, 0, 0, 0, 1, 1, 1, 1]


def test_sort_01_random_3():
    result = solution_04([1, 1, 1, 0, 0, 0, 1, 1, 0, 0])
    assert result == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def test_sort_01_random_4():
    result = solution_04([0, 0, 1, 1, 1, 0, 0, 1, 0, 1])
    assert result == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def test_sort_01_random_5():
    result = solution_04([1, 0, 0, 1, 0, 1, 0, 1, 0, 1])
    assert result == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]