import pytest
from homework_02.solutions import remove_element, linked_list_from_array, linked_list_to_array


def test_empty_list():
    """Пустой список должен остаться пустым"""
    assert remove_element(None, 5) is None


def test_single_element_match():
    """Список из одного элемента, который совпадает с val, должен стать пустым"""
    head = linked_list_from_array([5])
    result = remove_element(head, 5)
    assert result is None


def test_single_element_no_match():
    """Список из одного элемента, который не совпадает с val, должен остаться без изменений"""
    head = linked_list_from_array([5])
    result = remove_element(head, 3)
    assert linked_list_to_array(result) == [5]


def test_remove_head_element():
    """Удаление первого элемента списка"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    result = remove_element(head, 1)
    assert linked_list_to_array(result) == [2, 3, 4, 5]


def test_remove_tail_element():
    """Удаление последнего элемента списка"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    result = remove_element(head, 5)
    assert linked_list_to_array(result) == [1, 2, 3, 4]


def test_remove_middle_element():
    """Удаление элемента из середины списка"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    result = remove_element(head, 3)
    assert linked_list_to_array(result) == [1, 2, 4, 5]


def test_remove_multiple_occurrences():
    """Удаление всех элементов, совпадающих с val"""
    head = linked_list_from_array([1, 3, 2, 3, 4, 3, 5])
    result = remove_element(head, 3)
    assert linked_list_to_array(result) == [1, 2, 4, 5]


def test_no_matching_elements():
    """Если нет элементов, совпадающих с val, список должен остаться без изменений"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    result = remove_element(head, 10)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5]


def test_all_elements_match():
    """Если все элементы совпадают с val, список должен стать пустым"""
    head = linked_list_from_array([5, 5, 5, 5])
    result = remove_element(head, 5)
    assert result is None


def test_consecutive_matching_elements():
    """Удаление нескольких подряд идущих элементов"""
    head = linked_list_from_array([1, 2, 2, 2, 3, 4])
    result = remove_element(head, 2)
    assert linked_list_to_array(result) == [1, 3, 4]


def test_negative_values():
    """Удаление элемента с отрицательным значением"""
    head = linked_list_from_array([-5, -3, -1, 0, 2])
    result = remove_element(head, -3)
    assert linked_list_to_array(result) == [-5, -1, 0, 2]


def test_zero_value():
    """Удаление элемента со значением 0"""
    head = linked_list_from_array([1, 0, -1, 0, 2])
    result = remove_element(head, 0)
    assert linked_list_to_array(result) == [1, -1, 2]


def test_large_list():
    """Тест на большом списке (100 элементов)"""
    arr = list(range(1, 101))
    head = linked_list_from_array(arr)
    result = remove_element(head, 50)
    expected = list(range(1, 50)) + list(range(51, 101))
    assert linked_list_to_array(result) == expected


def test_remove_first_two_elements():
    """Удаление первых двух элементов, если они совпадают с val"""
    head = linked_list_from_array([3, 3, 1, 2, 3])
    result = remove_element(head, 3)
    assert linked_list_to_array(result) == [1, 2]


def test_preserve_node_references():
    """Убедиться, что узлы не копируются, а изменяются ссылки"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    original_second = head.next
    result = remove_element(head, 1)
    assert result is original_second
    assert linked_list_to_array(result) == [2, 3, 4, 5]


def test_val_not_in_list():
    """Значение val отсутствует в списке"""
    head = linked_list_from_array([10, 20, 30, 40])
    result = remove_element(head, 15)
    assert linked_list_to_array(result) == [10, 20, 30, 40]


def test_remove_from_two_element_list_head():
    """Удаление головы из списка двух элементов"""
    head = linked_list_from_array([1, 2])
    result = remove_element(head, 1)
    assert linked_list_to_array(result) == [2]


def test_remove_from_two_element_list_tail():
    """Удаление хвоста из списка двух элементов"""
    head = linked_list_from_array([1, 2])
    result = remove_element(head, 2)
    assert linked_list_to_array(result) == [1]