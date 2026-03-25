from homework_02.solutions import merge_linked_lists, linked_list_from_array, linked_list_to_array


def test_both_lists_empty():
    """Оба списка пустые — результат пустой"""
    assert merge_linked_lists(None, None) is None


def test_first_list_empty():
    """Первый список пустой — возвращается второй список"""
    list2 = linked_list_from_array([1, 2, 3])
    result = merge_linked_lists(None, list2)
    assert linked_list_to_array(result) == [1, 2, 3]


def test_second_list_empty():
    """Второй список пустой — возвращается первый список"""
    list1 = linked_list_from_array([1, 2, 3])
    result = merge_linked_lists(list1, None)
    assert linked_list_to_array(result) == [1, 2, 3]


def test_both_single_element():
    """Оба списка по одному элементу"""
    list1 = linked_list_from_array([1])
    list2 = linked_list_from_array([2])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2]


def test_both_single_element_reverse():
    """Оба списка по одному элементу (обратный порядок)"""
    list1 = linked_list_from_array([2])
    list2 = linked_list_from_array([1])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2]


def test_example_from_task():
    """Пример из задания"""
    list1 = linked_list_from_array([3, 6, 8])
    list2 = linked_list_from_array([4, 7, 9, 11])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [3, 4, 6, 7, 8, 9, 11]


def test_equal_length_lists():
    """Списки одинаковой длины"""
    list1 = linked_list_from_array([1, 3, 5])
    list2 = linked_list_from_array([2, 4, 6])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_first_list_longer():
    """Первый список длиннее второго"""
    list1 = linked_list_from_array([1, 3, 5, 7, 9])
    list2 = linked_list_from_array([2, 4])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 7, 9]


def test_second_list_longer():
    """Второй список длиннее первого"""
    list1 = linked_list_from_array([1, 3])
    list2 = linked_list_from_array([2, 4, 6, 8, 10])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 6, 8, 10]


def test_all_elements_first_smaller():
    """Все элементы первого списка меньше второго"""
    list1 = linked_list_from_array([1, 2, 3])
    list2 = linked_list_from_array([4, 5, 6])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_all_elements_second_smaller():
    """Все элементы второго списка меньше первого"""
    list1 = linked_list_from_array([4, 5, 6])
    list2 = linked_list_from_array([1, 2, 3])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 6]


def test_duplicate_values_within_lists():
    """Дубликаты значений внутри списков"""
    list1 = linked_list_from_array([1, 1, 3])
    list2 = linked_list_from_array([1, 2, 4])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 1, 1, 2, 3, 4]


def test_duplicate_values_across_lists():
    """Одинаковые значения в обоих списках"""
    list1 = linked_list_from_array([2, 4, 6])
    list2 = linked_list_from_array([2, 4, 6])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [2, 2, 4, 4, 6, 6]


def test_negative_numbers():
    """Отрицательные числа"""
    list1 = linked_list_from_array([-5, -3, -1])
    list2 = linked_list_from_array([-4, -2, 0])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [-5, -4, -3, -2, -1, 0]


def test_mixed_positive_negative():
    """Смешанные положительные и отрицательные числа"""
    list1 = linked_list_from_array([-3, 0, 3])
    list2 = linked_list_from_array([-2, 1, 4])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [-3, -2, 0, 1, 3, 4]


def test_zero_values():
    """Нулевые значения"""
    list1 = linked_list_from_array([-2, 0, 2])
    list2 = linked_list_from_array([-1, 0, 1])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [-2, -1, 0, 0, 1, 2]


def test_large_lists():
    """Большие списки (по 50 элементов каждый)"""
    list1 = linked_list_from_array(list(range(0, 100, 2)))
    list2 = linked_list_from_array(list(range(1, 100, 2)))
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == list(range(100))


def test_in_place_modification():
    """Убедиться, что узлы не копируются, а изменяются ссылки"""
    list1 = linked_list_from_array([1, 3, 5])
    list2 = linked_list_from_array([2, 4, 6])
    
    original_list1_head = list1
    original_list2_head = list2
    
    result = merge_linked_lists(list1, list2)
    
    assert result is original_list1_head or result is original_list2_head


def test_preserves_node_references():
    """Проверка, что узлы не создаются заново"""
    list1 = linked_list_from_array([1, 3])
    list2 = linked_list_from_array([2, 4])
    
    original_nodes = set()
    cur = list1
    while cur:
        original_nodes.add(id(cur))
        cur = cur.next
    cur = list2
    while cur:
        original_nodes.add(id(cur))
        cur = cur.next
    
    result = merge_linked_lists(list1, list2)
    
    result_nodes = set()
    cur = result
    while cur:
        result_nodes.add(id(cur))
        cur = cur.next
    
    assert original_nodes == result_nodes


def test_alternating_elements():
    """Чередующиеся элементы из двух списков"""
    list1 = linked_list_from_array([1, 3, 5, 7])
    list2 = linked_list_from_array([2, 4, 6, 8])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_first_element_from_second_list():
    """Первый элемент результата из второго списка"""
    list1 = linked_list_from_array([5, 6, 7])
    list2 = linked_list_from_array([1, 2, 3])
    result = merge_linked_lists(list1, list2)
    assert result.val == 1


def test_first_element_from_first_list():
    """Первый элемент результата из первого списка"""
    list1 = linked_list_from_array([1, 2, 3])
    list2 = linked_list_from_array([5, 6, 7])
    result = merge_linked_lists(list1, list2)
    assert result.val == 1


def test_last_elements_comparison():
    """Проверка последних элементов"""
    list1 = linked_list_from_array([1, 3, 5])
    list2 = linked_list_from_array([2, 4, 6])
    result = merge_linked_lists(list1, list2)
    
    cur = result
    while cur.next:
        cur = cur.next
    assert cur.val == 6


def test_one_element_each_same_value():
    """По одному элементу с одинаковым значением"""
    list1 = linked_list_from_array([5])
    list2 = linked_list_from_array([5])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [5, 5]


def test_many_duplicates():
    """Много дубликатов в обоих списках"""
    list1 = linked_list_from_array([1, 1, 1, 1])
    list2 = linked_list_from_array([1, 1, 1])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 1, 1, 1, 1, 1, 1]


def test_interleaved_with_gaps():
    """Списки с промежутками между значениями"""
    list1 = linked_list_from_array([1, 5, 10])
    list2 = linked_list_from_array([3, 7, 12])
    result = merge_linked_lists(list1, list2)
    assert linked_list_to_array(result) == [1, 3, 5, 7, 10, 12]


def test_result_is_sorted():
    """Результат должен быть отсортирован"""
    list1 = linked_list_from_array([1, 5, 9, 13])
    list2 = linked_list_from_array([2, 6, 10, 14])
    result = merge_linked_lists(list1, list2)
    result_array = linked_list_to_array(result)
    assert result_array == sorted(result_array)


def test_memory_efficiency():
    """Проверка, что не создается новых узлов (только dummy)"""
    list1 = linked_list_from_array([1, 2, 3])
    list2 = linked_list_from_array([4, 5, 6])
    
    count1 = 0
    cur = list1
    while cur:
        count1 += 1
        cur = cur.next
    
    count2 = 0
    cur = list2
    while cur:
        count2 += 1
        cur = cur.next
    
    result = merge_linked_lists(list1, list2)
    
    count_result = 0
    cur = result
    while cur:
        count_result += 1
        cur = cur.next
    
    assert count_result == count1 + count2