"""Тесты для подсчета подмассивов с суммой k"""
from homework_08.solutions import subarray_sum_equals_k


class TestSubarraySumEqualsK:
    def test_basic_case(self):
        """Стандартный пример с двумя подходящими подмассивами"""
        assert subarray_sum_equals_k([1, 1, 1], 2) == 2

    def test_multiple_solutions(self):
        """Несколько подмассивов могут иметь одинаковую целевую сумму"""
        assert subarray_sum_equals_k([1, 2, 3], 3) == 2

    def test_with_negative_values(self):
        """Алгоритм корректно работает с отрицательными числами"""
        assert subarray_sum_equals_k([1, -1, 0], 0) == 3

    def test_all_zeros(self):
        """Для массива из нулей количество подмассивов быстро растет"""
        assert subarray_sum_equals_k([0, 0, 0], 0) == 6

    def test_no_matching_subarray(self):
        """Если подходящих подмассивов нет, возвращается 0"""
        assert subarray_sum_equals_k([2, 4, 6], 5) == 0

    def test_empty_array(self):
        """В пустом массиве нет непрерывных подмассивов"""
        assert subarray_sum_equals_k([], 0) == 0