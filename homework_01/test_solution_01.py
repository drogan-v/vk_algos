from homework_01.solutions import solution_01


# ==================== Базовые тесты ====================

def test_rotate_empty_array():
    result = solution_01([], 3)
    assert result == []


def test_rotate_single_element():
    result = solution_01([5], 1)
    assert result == [5]


def test_rotate_single_element_k0():
    result = solution_01([5], 0)
    assert result == [5]


# ==================== k = 0 (без сдвига) ====================

def test_rotate_k0_three_elements():
    result = solution_01([1, 2, 3], 0)
    assert result == [1, 2, 3]


def test_rotate_k0_five_elements():
    result = solution_01([1, 2, 3, 4, 5], 0)
    assert result == [1, 2, 3, 4, 5]


# ==================== k = 1 ====================

def test_rotate_k1_two_elements():
    result = solution_01([1, 2], 1)
    assert result == [2, 1]


def test_rotate_k1_three_elements():
    result = solution_01([1, 2, 3], 1)
    assert result == [3, 1, 2]


def test_rotate_k1_five_elements():
    result = solution_01([1, 2, 3, 4, 5], 1)
    assert result == [5, 1, 2, 3, 4]


def test_rotate_k1_seven_elements():
    result = solution_01([1, 2, 3, 4, 5, 6, 7], 1)
    assert result == [7, 1, 2, 3, 4, 5, 6]


# ==================== k = n (полный оборот) ====================

def test_rotate_k_equals_n_three():
    result = solution_01([1, 2, 3], 3)
    assert result == [1, 2, 3]


def test_rotate_k_equals_n_five():
    result = solution_01([1, 2, 3, 4, 5], 5)
    assert result == [1, 2, 3, 4, 5]


# ==================== k > n (k modulo n) ====================

def test_rotate_k_greater_than_n():
    result = solution_01([1, 2, 3], 4)  # 4 % 3 = 1
    assert result == [3, 1, 2]


def test_rotate_k_much_greater():
    result = solution_01([1, 2, 3], 10)  # 10 % 3 = 1
    assert result == [3, 1, 2]


def test_rotate_k_multiple_of_n():
    result = solution_01([1, 2, 3, 4], 8)  # 8 % 4 = 0
    assert result == [1, 2, 3, 4]


# ==================== k = n - 1 ====================

def test_rotate_k_n_minus_1_three():
    result = solution_01([1, 2, 3], 2)
    assert result == [2, 3, 1]


def test_rotate_k_n_minus_1_five():
    result = solution_01([1, 2, 3, 4, 5], 4)
    assert result == [2, 3, 4, 5, 1]


# ==================== Два элемента ====================

def test_rotate_two_k0():
    result = solution_01([1, 2], 0)
    assert result == [1, 2]


def test_rotate_two_k1():
    result = solution_01([1, 2], 1)
    assert result == [2, 1]


def test_rotate_two_k2():
    result = solution_01([1, 2], 2)
    assert result == [1, 2]


# ==================== Три элемента ====================

def test_rotate_three_k0():
    result = solution_01([1, 2, 3], 0)
    assert result == [1, 2, 3]


def test_rotate_three_k1():
    result = solution_01([1, 2, 3], 1)
    assert result == [3, 1, 2]


def test_rotate_three_k2():
    result = solution_01([1, 2, 3], 2)
    assert result == [2, 3, 1]


# ==================== Четыре элемента ====================

def test_rotate_four_k1():
    result = solution_01([1, 2, 3, 4], 1)
    assert result == [4, 1, 2, 3]


def test_rotate_four_k2():
    result = solution_01([1, 2, 3, 4], 2)
    assert result == [3, 4, 1, 2]


def test_rotate_four_k3():
    result = solution_01([1, 2, 3, 4], 3)
    assert result == [2, 3, 4, 1]


# ==================== Пять элементов ====================

def test_rotate_five_k1():
    result = solution_01([1, 2, 3, 4, 5], 1)
    assert result == [5, 1, 2, 3, 4]


def test_rotate_five_k2():
    result = solution_01([1, 2, 3, 4, 5], 2)
    assert result == [4, 5, 1, 2, 3]


def test_rotate_five_k3():
    result = solution_01([1, 2, 3, 4, 5], 3)
    assert result == [3, 4, 5, 1, 2]


def test_rotate_five_k4():
    result = solution_01([1, 2, 3, 4, 5], 4)
    assert result == [2, 3, 4, 5, 1]


# ==================== Отрицательные числа ====================

def test_rotate_negative():
    result = solution_01([-1, -2, -3, -4, -5], 2)
    assert result == [-4, -5, -1, -2, -3]


def test_rotate_mixed():
    result = solution_01([1, -2, 3, -4, 5], 2)
    assert result == [-4, 5, 1, -2, 3]


# ==================== Большие массивы ====================

def test_rotate_ten_k1():
    result = solution_01(list(range(1, 11)), 1)
    assert result == [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_rotate_ten_k5():
    result = solution_01(list(range(1, 11)), 5)
    assert result == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]


def test_rotate_ten_k15():
    result = solution_01(list(range(1, 11)), 15)  # 15 % 10 = 5
    assert result == [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]


# ==================== Классические примеры (LeetCode 189) ====================

def test_rotate_leetcode_example1():
    result = solution_01([1, 2, 3, 4, 5, 6, 7], 3)
    assert result == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_leetcode_example2():
    result = solution_01([-1, -100, 3, 99], 2)
    assert result == [3, 99, -1, -100]


# ==================== Все одинаковые элементы ====================

def test_rotate_all_same():
    result = solution_01([5, 5, 5, 5], 2)
    assert result == [5, 5, 5, 5]


# ==================== Граничные значения k ====================

def test_rotate_k_very_large():
    result = solution_01([1, 2, 3], 1000000)  # 1000000 % 3 = 1
    assert result == [3, 1, 2]


def test_rotate_k_zero_large_array():
    result = solution_01(list(range(100)), 0)
    assert result == list(range(100))


# ==================== Специфические паттерны ====================

def test_rotate_sorted_array():
    result = solution_01([1, 2, 3, 4, 5, 6, 7], 3)
    assert result == [5, 6, 7, 1, 2, 3, 4]


def test_rotate_reverse_sorted():
    result = solution_01([7, 6, 5, 4, 3, 2, 1], 3)
    assert result == [3, 2, 1, 7, 6, 5, 4]


def test_rotate_with_zero():
    result = solution_01([0, 1, 2, 3, 4], 2)
    assert result == [3, 4, 0, 1, 2]


# ==================== Разные размеры массивов ====================

def test_rotate_size_6_k2():
    result = solution_01([1, 2, 3, 4, 5, 6], 2)
    assert result == [5, 6, 1, 2, 3, 4]


def test_rotate_size_6_k3():
    result = solution_01([1, 2, 3, 4, 5, 6], 3)
    assert result == [4, 5, 6, 1, 2, 3]


def test_rotate_size_8_k3():
    result = solution_01([1, 2, 3, 4, 5, 6, 7, 8], 3)
    assert result == [6, 7, 8, 1, 2, 3, 4, 5]


def test_rotate_size_8_k5():
    result = solution_01([1, 2, 3, 4, 5, 6, 7, 8], 5)
    assert result == [4, 5, 6, 7, 8, 1, 2, 3]


# ==================== Случайные тесты ====================

def test_rotate_random_1():
    result = solution_01([5, 1, 8, 3, 9, 2], 3)
    assert result == [3, 9, 2, 5, 1, 8]


def test_rotate_random_2():
    result = solution_01([10, 20, 30, 40, 50], 4)
    assert result == [20, 30, 40, 50, 10]


def test_rotate_random_3():
    result = solution_01([7, 3, 9, 1, 5, 8, 2], 5)
    assert result == [9, 1, 5, 8, 2, 7, 3]