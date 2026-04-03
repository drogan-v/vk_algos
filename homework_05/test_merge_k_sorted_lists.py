"""Тесты для слияния k отсортированных списков"""
from homework_05.solutions import merge_k_sorted_lists


class TestMergeKSortedLists:
    def test_empty_lists(self):
        """Список пустых списков"""
        assert merge_k_sorted_lists([]) == []
        assert merge_k_sorted_lists([[], [], []]) == []

    def test_single_list(self):
        """Один список"""
        assert merge_k_sorted_lists([[1, 2, 3]]) == [1, 2, 3]

    def test_two_lists(self):
        """Два отсортированных списка"""
        result = merge_k_sorted_lists([[1, 3, 5], [2, 4, 6]])
        assert result == [1, 2, 3, 4, 5, 6]

    def test_multiple_lists(self):
        """Несколько отсортированных списков"""
        result = merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_lists_with_different_lengths(self):
        """Списки разной длины"""
        result = merge_k_sorted_lists([[1], [2, 3], [4, 5, 6]])
        assert result == [1, 2, 3, 4, 5, 6]

    def test_duplicate_elements(self):
        """Списки с дублирующимися элементами"""
        result = merge_k_sorted_lists([[1, 1], [1, 2], [1, 3]])
        assert result == [1, 1, 1, 1, 2, 3]
