import pytest
from homework_02.solutions import reverse_linked_list, linked_list_from_array, linked_list_to_array


def test_empty_list():
    """Пустой список должен остаться пустым"""
    assert reverse_linked_list(None) is None

def test_single_element():
    """Список из одного элемента должен остаться без изменений"""
    head = linked_list_from_array([5])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == [5]

def test_two_elements():
    """Список из двух элементов должен поменять их местами"""
    head = linked_list_from_array([1, 2])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == [2, 1]

def test_multiple_elements():
    """Список из нескольких элементов должен быть полностью развернут"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == [5, 4, 3, 2, 1]

def test_all_same_values():
    """Список с одинаковыми значениями должен корректно развернуться"""
    head = linked_list_from_array([3, 3, 3, 3])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == [3, 3, 3, 3]

def test_negative_values():
    """Список с отрицательными значениями должен корректно развернуться"""
    head = linked_list_from_array([-1, -2, -3])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == [-3, -2, -1]

def test_mixed_values():
    """Список с положительными и отрицательными значениями"""
    head = linked_list_from_array([-5, 0, 3, -1, 7])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == [7, -1, 3, 0, -5]

def test_in_place_modification():
    """Убедиться, что разворот происходит in-place (изменяются ссылки)"""
    head = linked_list_from_array([1, 2, 3])
    original_head = head
    
    # После разворота original_head должен стать последним узлом
    reversed_head = reverse_linked_list(head)
    
    # Проверяем, что первый узел теперь указывает на None
    assert original_head.next is None
    # Проверяем, что новый head - это последний узел исходного списка
    assert reversed_head.val == 3

def test_large_list():
    """Тест на большом списке (100 элементов)"""
    arr = list(range(100))
    head = linked_list_from_array(arr)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_array(reversed_head) == list(range(99, -1, -1))
