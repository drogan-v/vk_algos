from homework_01.solutions import solution_02


# ==================== Базовые тесты ====================

def test_merge_both_empty():
    result = solution_02([], [])
    assert result == []


def test_merge_first_empty():
    result = solution_02([], [1, 2, 3])
    assert result == [1, 2, 3]


def test_merge_second_empty():
    result = solution_02([1, 2, 3], [])
    assert result == [1, 2, 3]


def test_merge_single_elements():
    result = solution_02([1], [2])
    assert result == [1, 2]


def test_merge_single_elements_reverse():
    result = solution_02([2], [1])
    assert result == [1, 2]


# ==================== Одинаковый размер массивов ====================

def test_merge_equal_size_2():
    result = solution_02([1, 3], [2, 4])
    assert result == [1, 2, 3, 4]


def test_merge_equal_size_3():
    result = solution_02([1, 3, 5], [2, 4, 6])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_equal_size_4():
    result = solution_02([1, 3, 5, 7], [2, 4, 6, 8])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_equal_size_5():
    result = solution_02([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==================== Разный размер массивов ====================

def test_merge_first_smaller():
    result = solution_02([1, 2], [3, 4, 5, 6, 7])
    assert result == [1, 2, 3, 4, 5, 6, 7]


def test_merge_first_larger():
    result = solution_02([1, 2, 3, 4, 5], [6, 7])
    assert result == [1, 2, 3, 4, 5, 6, 7]


def test_merge_first_much_smaller():
    result = solution_02([1], [2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_first_much_larger():
    result = solution_02([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


# ==================== Все элементы одинаковые ====================

def test_merge_all_same_first():
    result = solution_02([5, 5, 5], [1, 1, 1])
    assert result == [1, 1, 1, 5, 5, 5]


def test_merge_all_same_second():
    result = solution_02([1, 1, 1], [5, 5, 5])
    assert result == [1, 1, 1, 5, 5, 5]


def test_merge_all_same_both():
    result = solution_02([3, 3, 3], [3, 3, 3])
    assert result == [3, 3, 3, 3, 3, 3]


# ==================== Дубликаты ====================

def test_merge_with_duplicates_1():
    result = solution_02([1, 2, 2, 3], [2, 3, 4])
    assert result == [1, 2, 2, 2, 3, 3, 4]


def test_merge_with_duplicates_2():
    result = solution_02([1, 1, 1], [1, 1, 1])
    assert result == [1, 1, 1, 1, 1, 1]


def test_merge_with_duplicates_3():
    result = solution_02([1, 3, 3, 5], [2, 3, 3, 6])
    assert result == [1, 2, 3, 3, 3, 3, 5, 6]


def test_merge_with_duplicates_4():
    result = solution_02([1, 1, 2, 2], [1, 2, 2, 3])
    assert result == [1, 1, 1, 2, 2, 2, 2, 3]


# ==================== Отрицательные числа ====================

def test_merge_negative_numbers():
    result = solution_02([-5, -3, -1], [-4, -2, 0])
    assert result == [-5, -4, -3, -2, -1, 0]


def test_merge_mixed_positive_negative():
    result = solution_02([-3, -1, 0], [1, 2, 3])
    assert result == [-3, -1, 0, 1, 2, 3]


def test_merge_all_negative():
    result = solution_02([-5, -3, -1], [-4, -2, -1])
    assert result == [-5, -4, -3, -2, -1, -1]


def test_merge_negative_and_positive():
    result = solution_02([-10, -5, 0], [5, 10, 15])
    assert result == [-10, -5, 0, 5, 10, 15]


# ==================== Один элемент в одном массиве ====================

def test_merge_one_in_first():
    result = solution_02([5], [1, 2, 3, 4, 6, 7, 8])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_one_in_second():
    result = solution_02([1, 2, 3, 4, 6, 7, 8], [5])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_one_in_first_beginning():
    result = solution_02([1], [2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_merge_one_in_first_end():
    result = solution_02([10], [1, 2, 3, 4])
    assert result == [1, 2, 3, 4, 10]


def test_merge_one_in_second_beginning():
    result = solution_02([2, 3, 4, 5], [1])
    assert result == [1, 2, 3, 4, 5]


def test_merge_one_in_second_end():
    result = solution_02([1, 2, 3, 4], [5])
    assert result == [1, 2, 3, 4, 5]


# ==================== Чередование элементов ====================

def test_merge_alternating():
    result = solution_02([1, 3, 5, 7], [2, 4, 6, 8])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_alternating_reverse():
    result = solution_02([2, 4, 6, 8], [1, 3, 5, 7])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_merge_alternating_odd():
    result = solution_02([1, 3, 5], [2, 4, 6])
    assert result == [1, 2, 3, 4, 5, 6]


# ==================== Один массив полностью меньше другого ====================

def test_merge_first_all_smaller():
    result = solution_02([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_first_all_larger():
    result = solution_02([4, 5, 6], [1, 2, 3])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_first_all_smaller_large():
    result = solution_02([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_merge_first_all_larger_large():
    result = solution_02([6, 7, 8, 9, 10], [1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==================== Большие массивы ====================

def test_merge_large_arrays():
    result = solution_02(list(range(0, 100, 2)), list(range(1, 100, 2)))
    assert result == list(range(100))


def test_merge_large_arrays_reverse():
    result = solution_02(list(range(1, 100, 2)), list(range(0, 100, 2)))
    assert result == list(range(100))


def test_merge_large_same_size():
    arr1 = list(range(0, 50))
    arr2 = list(range(50, 100))
    result = solution_02(arr1, arr2)
    assert result == list(range(100))


# ==================== Граничные значения ====================

def test_merge_with_zero():
    result = solution_02([-2, -1, 0], [0, 1, 2])
    assert result == [-2, -1, 0, 0, 1, 2]


def test_merge_with_max_int():
    result = solution_02([1, 2, 3], [2147483647])
    assert result == [1, 2, 3, 2147483647]


def test_merge_with_min_int():
    result = solution_02([-2147483648], [1, 2, 3])
    assert result == [-2147483648, 1, 2, 3]


# ==================== Специфические паттерны ====================

def test_merge_interleaved_1():
    result = solution_02([1, 5, 9], [2, 6, 10])
    assert result == [1, 2, 5, 6, 9, 10]


def test_merge_interleaved_2():
    result = solution_02([1, 10, 20], [5, 15, 25])
    assert result == [1, 5, 10, 15, 20, 25]


def test_merge_close_values():
    result = solution_02([1, 2, 3], [1, 2, 3])
    assert result == [1, 1, 2, 2, 3, 3]


def test_merge_overlapping_ranges():
    result = solution_02([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    assert result == [1, 2, 3, 3, 4, 4, 5, 5, 6, 7]


# ==================== Классические примеры ====================

def test_merge_classic_1():
    result = solution_02([1, 3, 5], [2, 4, 6])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_classic_2():
    result = solution_02([1, 2, 3], [4, 5, 6])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_classic_3():
    result = solution_02([4, 5, 6], [1, 2, 3])
    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_classic_4():
    result = solution_02([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==================== Случайные тесты ====================

def test_merge_random_1():
    result = solution_02([1, 5, 8, 10], [2, 3, 7, 9])
    assert result == [1, 2, 3, 5, 7, 8, 9, 10]


def test_merge_random_2():
    result = solution_02([0, 2, 4, 6], [1, 3, 5, 7])
    assert result == [0, 1, 2, 3, 4, 5, 6, 7]


def test_merge_random_3():
    result = solution_02([10, 20, 30], [15, 25, 35])
    assert result == [10, 15, 20, 25, 30, 35]


def test_merge_random_4():
    result = solution_02([-5, 0, 5], [-3, 2, 7])
    assert result == [-5, -3, 0, 2, 5, 7]


def test_merge_random_5():
    result = solution_02([1, 1, 3, 3], [2, 2, 4, 4])
    assert result == [1, 1, 2, 2, 3, 3, 4, 4]