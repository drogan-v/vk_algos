"""Тесты для максимальной длины подмассива с равным числом 0 и 1"""
from homework_08.solutions import max_equal_zero_one_subarray_length


class TestMaxEqualZeroOneSubarrayLength:
    def test_basic_case(self):
        """Базовый случай: весь массив сбалансирован"""
        assert max_equal_zero_one_subarray_length([0, 1]) == 2

    def test_longer_balanced_subarray(self):
        """Максимум может быть не в начале"""
        assert max_equal_zero_one_subarray_length([0, 1, 0, 1, 1]) == 4

    def test_all_zeros(self):
        """Если только нули, сбалансированного подмассива нет"""
        assert max_equal_zero_one_subarray_length([0, 0, 0]) == 0

    def test_all_ones(self):
        """Если только единицы, сбалансированного подмассива нет"""
        assert max_equal_zero_one_subarray_length([1, 1, 1, 1]) == 0

    def test_mixed_full_length(self):
        """Весь массив может быть ответом"""
        assert max_equal_zero_one_subarray_length([0, 0, 1, 1, 0, 1]) == 6

    def test_empty_array(self):
        """Для пустого массива длина 0"""
        assert max_equal_zero_one_subarray_length([]) == 0