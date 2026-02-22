from homework_01.solutions import solution_05
import pytest


# ==================== Базовые тесты ====================

def test_netherland_flag_empty():
    result = []
    solution_05(result)
    assert result == []


def test_netherland_flag_single_0():
    result = [0]
    solution_05(result)
    assert result == [0]


def test_netherland_flag_single_1():
    result = [1]
    solution_05(result)
    assert result == [1]


def test_netherland_flag_single_2():
    result = [2]
    solution_05(result)
    assert result == [2]


# ==================== Все одинаковые элементы ====================

def test_netherland_flag_all_zeros():
    result = [0, 0, 0, 0]
    solution_05(result)
    assert result == [0, 0, 0, 0]


def test_netherland_flag_all_ones():
    result = [1, 1, 1, 1]
    solution_05(result)
    assert result == [1, 1, 1, 1]


def test_netherland_flag_all_twos():
    result = [2, 2, 2, 2]
    solution_05(result)
    assert result == [2, 2, 2, 2]


# ==================== Два типа элементов ====================

def test_netherland_flag_only_0_and_1():
    result = [1, 0, 1, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1]


def test_netherland_flag_only_0_and_2():
    result = [2, 0, 2, 0]
    solution_05(result)
    assert result == [0, 0, 2, 2]


def test_netherland_flag_only_1_and_2():
    result = [2, 1, 2, 1]
    solution_05(result)
    assert result == [1, 1, 2, 2]


def test_netherland_flag_0_1_already_sorted():
    result = [0, 0, 1, 1]
    solution_05(result)
    assert result == [0, 0, 1, 1]


def test_netherland_flag_0_1_reverse():
    result = [1, 1, 0, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1]


# ==================== Все три типа элементов ====================

def test_netherland_flag_basic():
    result = [2, 0, 2, 1, 1, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


def test_netherland_flag_three_elements():
    result = [0, 1, 2]
    solution_05(result)
    assert result == [0, 1, 2]


def test_netherland_flag_three_elements_reverse():
    result = [2, 1, 0]
    solution_05(result)
    assert result == [0, 1, 2]


def test_netherland_flag_three_types_mixed():
    result = [1, 2, 0, 1, 2, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


def test_netherland_flag_three_types_already_sorted():
    result = [0, 0, 1, 1, 2, 2]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


def test_netherland_flag_three_types_reverse_sorted():
    result = [2, 2, 1, 1, 0, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


# ==================== Граничные случаи ====================

def test_netherland_flag_single_zero():
    result = [0, 1, 1, 1]
    solution_05(result)
    assert result == [0, 1, 1, 1]


def test_netherland_flag_single_one():
    result = [0, 0, 1, 0]
    solution_05(result)
    assert result == [0, 0, 0, 1]


def test_netherland_flag_single_two():
    result = [0, 0, 2, 0]
    solution_05(result)
    assert result == [0, 0, 0, 2]


def test_netherland_flag_zero_at_end():
    result = [1, 1, 1, 0]
    solution_05(result)
    assert result == [0, 1, 1, 1]


def test_netherland_flag_two_at_start():
    result = [2, 0, 0, 0]
    solution_05(result)
    assert result == [0, 0, 0, 2]


# ==================== Два элемента ====================

def test_netherland_flag_two_0_0():
    result = [0, 0]
    solution_05(result)
    assert result == [0, 0]


def test_netherland_flag_two_0_1():
    result = [0, 1]
    solution_05(result)
    assert result == [0, 1]


def test_netherland_flag_two_0_2():
    result = [0, 2]
    solution_05(result)
    assert result == [0, 2]


def test_netherland_flag_two_1_0():
    result = [1, 0]
    solution_05(result)
    assert result == [0, 1]


def test_netherland_flag_two_1_2():
    result = [1, 2]
    solution_05(result)
    assert result == [1, 2]


def test_netherland_flag_two_2_0():
    result = [2, 0]
    solution_05(result)
    assert result == [0, 2]


def test_netherland_flag_two_2_1():
    result = [2, 1]
    solution_05(result)
    assert result == [1, 2]


def test_netherland_flag_two_1_1():
    result = [1, 1]
    solution_05(result)
    assert result == [1, 1]


def test_netherland_flag_two_2_2():
    result = [2, 2]
    solution_05(result)
    assert result == [2, 2]


# ==================== Три элемента (все комбинации) ====================

def test_netherland_flag_three_0_0_0():
    result = [0, 0, 0]
    solution_05(result)
    assert result == [0, 0, 0]


def test_netherland_flag_three_0_0_1():
    result = [0, 0, 1]
    solution_05(result)
    assert result == [0, 0, 1]


def test_netherland_flag_three_0_1_0():
    result = [0, 1, 0]
    solution_05(result)
    assert result == [0, 0, 1]


def test_netherland_flag_three_0_1_2():
    result = [0, 1, 2]
    solution_05(result)
    assert result == [0, 1, 2]


def test_netherland_flag_three_1_0_0():
    result = [1, 0, 0]
    solution_05(result)
    assert result == [0, 0, 1]


def test_netherland_flag_three_1_0_2():
    result = [1, 0, 2]
    solution_05(result)
    assert result == [0, 1, 2]


def test_netherland_flag_three_2_0_0():
    result = [2, 0, 0]
    solution_05(result)
    assert result == [0, 0, 2]


def test_netherland_flag_three_2_1_0():
    result = [2, 1, 0]
    solution_05(result)
    assert result == [0, 1, 2]


def test_netherland_flag_three_2_2_2():
    result = [2, 2, 2]
    solution_05(result)
    assert result == [2, 2, 2]


# ==================== Специфические паттерны ====================

def test_netherland_flag_alternating_0_1_2():
    result = [0, 1, 2, 0, 1, 2]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


def test_netherland_flag_alternating_2_1_0():
    result = [2, 1, 0, 2, 1, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


def test_netherland_flag_zigzag():
    result = [0, 2, 1, 2, 1, 0]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2]


def test_netherland_flag_random_order_1():
    result = [1, 0, 2, 1, 0, 2, 1]
    solution_05(result)
    assert result == [0, 0, 1, 1, 1, 2, 2]


def test_netherland_flag_random_order_2():
    result = [2, 2, 0, 0, 1, 1, 2]
    solution_05(result)
    assert result == [0, 0, 1, 1, 2, 2, 2]


# ==================== Большие массивы ====================

def test_netherland_flag_large_20_elements():
    result = [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    solution_05(result)
    assert result == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]


def test_netherland_flag_sorted_15_elements():
    result = [0]*5 + [1]*5 + [2]*5
    solution_05(result)
    assert result == [0]*5 + [1]*5 + [2]*5


def test_netherland_flag_reverse_sorted_15_elements():
    result = [2]*5 + [1]*5 + [0]*5
    solution_05(result)
    assert result == [0]*5 + [1]*5 + [2]*5


# ==================== Случайные тесты ====================

def test_netherland_flag_random_1():
    result = [1, 2, 0, 2, 1, 0, 1, 2, 0]
    solution_05(result)
    assert result == sorted([1, 2, 0, 2, 1, 0, 1, 2, 0])


def test_netherland_flag_random_2():
    result = [0, 2, 1, 0, 2, 1, 0, 2, 1, 0]
    solution_05(result)
    assert result == sorted([0, 2, 1, 0, 2, 1, 0, 2, 1, 0])


def test_netherland_flag_random_3():
    result = [2, 2, 2, 1, 1, 0, 0, 0, 1, 2]
    solution_05(result)
    assert result == sorted([2, 2, 2, 1, 1, 0, 0, 0, 1, 2])