"""Тесты для максимальной суммы подмассива длины k"""
import pytest

from homework_08.solutions import max_subarray_sum


class TestMaxSubarraySum:
    def test_basic_case(self):
        """Базовый пример с положительными числами"""
        assert max_subarray_sum([1, 2, 3, 4, 5], 2) == 9

    def test_mixed_numbers(self):
        """Смешанные положительные и отрицательные значения"""
        assert max_subarray_sum([2, -1, 5, -2, 3], 3) == 6

    def test_all_negative(self):
        """Если все числа отрицательные, выбираем наибольшую (наименее отрицательную) сумму"""
        assert max_subarray_sum([-5, -2, -3, -4], 2) == -5

    def test_k_equals_one(self):
        """При k=1 ответ равен максимальному элементу"""
        assert max_subarray_sum([4, 1, 7, 3], 1) == 7

    def test_k_equals_array_length(self):
        """При k равном длине массива ответ равен сумме всего массива"""
        assert max_subarray_sum([3, 1, 2], 3) == 6

    def test_invalid_k_zero(self):
        """k должно быть положительным"""
        with pytest.raises(ValueError):
            max_subarray_sum([1, 2, 3], 0)

    def test_invalid_k_too_large(self):
        """k не может быть больше длины массива"""
        with pytest.raises(ValueError):
            max_subarray_sum([1, 2, 3], 4)