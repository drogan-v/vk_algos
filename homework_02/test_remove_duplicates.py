import pytest
from homework_02.solutions import remove_duplicates


def test_empty_array():
    """Пустой массив должен вернуть 0"""
    assert remove_duplicates([]) == 0


def test_single_element():
    """Массив из одного элемента должен вернуть 1"""
    assert remove_duplicates([1]) == 1


def test_single_element_empty_after():
    """Массив из одного элемента остается без изменений"""
    arr = [5]
    length = remove_duplicates(arr)
    assert length == 1
    assert arr[:length] == [5]


def test_two_elements_same():
    """Два одинаковых элемента должны стать одним"""
    arr = [1, 1]
    length = remove_duplicates(arr)
    assert length == 1
    assert arr[:length] == [1]


def test_two_elements_different():
    """Два разных элемента должны остаться без изменений"""
    arr = [1, 2]
    length = remove_duplicates(arr)
    assert length == 2
    assert arr[:length] == [1, 2]


def test_all_elements_same():
    """Все элементы одинаковые — должен остаться один"""
    arr = [3, 3, 3, 3, 3]
    length = remove_duplicates(arr)
    assert length == 1
    assert arr[:length] == [3]


def test_all_elements_different():
    """Все элементы разные — длина не меняется"""
    arr = [1, 2, 3, 4, 5]
    length = remove_duplicates(arr)
    assert length == 5
    assert arr[:length] == [1, 2, 3, 4, 5]


def test_duplicates_at_beginning():
    """Дубликаты в начале массива"""
    arr = [1, 1, 2, 3, 4]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 4]


def test_duplicates_at_end():
    """Дубликаты в конце массива"""
    arr = [1, 2, 3, 4, 4]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 4]


def test_duplicates_in_middle():
    """Дубликаты в середине массива"""
    arr = [1, 2, 2, 2, 3, 4]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 4]


def test_multiple_duplicate_groups():
    """Несколько групп дубликатов"""
    arr = [1, 1, 2, 2, 3, 3, 4, 4]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 4]


def test_negative_numbers():
    """Отрицательные числа"""
    arr = [-5, -5, -3, -1, -1, 0]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [-5, -3, -1, 0]


def test_mixed_positive_negative():
    """Смешанные положительные и отрицательные числа"""
    arr = [-3, -3, -1, 0, 0, 2, 2, 5]
    length = remove_duplicates(arr)
    assert length == 5
    assert arr[:length] == [-3, -1, 0, 2, 5]


def test_zero_values():
    """Нулевые значения"""
    arr = [0, 0, 0, 1, 1, 2]
    length = remove_duplicates(arr)
    assert length == 3
    assert arr[:length] == [0, 1, 2]


def test_large_array():
    """Большой массив (100 элементов)"""
    arr = []
    for i in range(20):
        arr.extend([i] * 5)
    length = remove_duplicates(arr)
    assert length == 20
    assert arr[:length] == list(range(20))


def test_three_consecutive_duplicates():
    """Три подряд идущих дубликата"""
    arr = [1, 2, 2, 2, 3]
    length = remove_duplicates(arr)
    assert length == 3
    assert arr[:length] == [1, 2, 3]


def test_five_consecutive_duplicates():
    """Пять подряд идущих дубликатов"""
    arr = [1, 2, 2, 2, 2, 2, 3]
    length = remove_duplicates(arr)
    assert length == 3
    assert arr[:length] == [1, 2, 3]


def test_in_place_modification():
    """Убедиться, что массив модифицируется in-place"""
    arr = [1, 1, 2, 3, 3]
    original_id = id(arr)
    length = remove_duplicates(arr)
    assert id(arr) == original_id
    assert length == 3
    assert arr[:length] == [1, 2, 3]


def test_returned_length_matches_unique_count():
    """Возвращенная длина равна количеству уникальных элементов"""
    arr = [1, 1, 2, 2, 3, 3, 4, 5, 5]
    length = remove_duplicates(arr)
    assert length == len(set(arr))
    assert arr[:length] == sorted(list(set(arr)))


def test_array_with_one_unique():
    """Массив с одним уникальным элементом (много дубликатов)"""
    arr = [7] * 50
    length = remove_duplicates(arr)
    assert length == 1
    assert arr[:length] == [7]


def test_array_with_all_unique():
    """Массив где все элементы уникальны"""
    arr = list(range(1, 101))
    length = remove_duplicates(arr)
    assert length == 100
    assert arr[:length] == list(range(1, 101))


def test_preserves_order():
    """Порядок элементов сохраняется"""
    arr = [1, 1, 2, 2, 3, 3]
    length = remove_duplicates(arr)
    assert arr[:length] == [1, 2, 3]


def test_slow_fast_pointer_logic():
    """Проверка логики работы медленного и быстрого указателей"""
    arr = [1, 1, 2, 3, 3, 4]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 4]


def test_consecutive_duplicates_various_lengths():
    """Дубликаты различной длины подряд"""
    arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 4]


def test_first_element_duplicate():
    """Первый элемент имеет дубликаты"""
    arr = [5, 5, 6, 7, 8]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [5, 6, 7, 8]


def test_last_element_duplicate():
    """Последний элемент имеет дубликаты"""
    arr = [1, 2, 3, 7, 7]
    length = remove_duplicates(arr)
    assert length == 4
    assert arr[:length] == [1, 2, 3, 7]