"""Тесты для поиска K-ого наименьшего в массиве"""
import pytest
from homework_05.solutions import find_kth_smallest_array


class TestFindKthSmallestArray:
    """Тесты для поиска K-ого наименьшего в массиве"""

    def test_k_equals_1(self):
        """K = 1, ищем минимум"""
        assert find_kth_smallest_array([3, 1, 4, 1, 5, 9], 1) == 1

    def test_k_equals_n(self):
        """K = n, ищем максимум"""
        assert find_kth_smallest_array([3, 1, 4, 1, 5, 9], 6) == 9

    def test_k_in_middle(self):
        """K в середине диапазона"""
        assert find_kth_smallest_array([3, 1, 4, 1, 5, 9], 3) == 3

    def test_unsorted_array(self):
        """Неотсортированный массив"""
        assert find_kth_smallest_array([7, 2, 9, 1, 5], 2) == 2

    def test_duplicate_elements(self):
        """Массив с дублирующимися элементами"""
        assert find_kth_smallest_array([5, 5, 5, 1, 1], 2) == 1

    def test_invalid_k_too_large(self):
        """K больше размера массива"""
        with pytest.raises(ValueError):
            find_kth_smallest_array([1, 2, 3], 5)

    def test_invalid_k_zero(self):
        """K = 0"""
        with pytest.raises(ValueError):
            find_kth_smallest_array([1, 2, 3], 0)
