"""Тесты для поиска индекса поворота массива"""
import pytest

from homework_08.solutions import find_rotation_index


class TestFindRotationIndex:
    def test_not_rotated_array(self):
        """Если массив не повернут, индекс минимального элемента равен 0"""
        assert find_rotation_index([1, 2, 3, 4, 5]) == 0

    def test_rotated_array(self):
        """Базовый случай с поворотом в середине"""
        assert find_rotation_index([4, 5, 6, 1, 2, 3]) == 3

    def test_rotation_near_end(self):
        """Поворот может быть в конце массива"""
        assert find_rotation_index([2, 3, 4, 5, 1]) == 4

    def test_rotation_near_start(self):
        """Поворот может быть почти в начале"""
        assert find_rotation_index([5, 1, 2, 3, 4]) == 1

    def test_single_element(self):
        """Для массива из одного элемента ответ всегда 0"""
        assert find_rotation_index([10]) == 0

    def test_two_elements_rotated(self):
        """Проверка минимального непустого поворота"""
        assert find_rotation_index([2, 1]) == 1

    def test_empty_array_raises_error(self):
        """Для пустого массива ожидаем ошибку"""
        with pytest.raises(ValueError):
            find_rotation_index([])