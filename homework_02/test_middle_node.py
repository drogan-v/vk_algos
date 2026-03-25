from homework_02.solutions import middle_node, linked_list_from_array, linked_list_to_array


def test_empty_list():
    """Пустой список должен вернуть None"""
    assert middle_node(None) is None


def test_single_element():
    """Список из одного элемента должен вернуть этот элемент"""
    head = linked_list_from_array([5])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 5


def test_two_elements():
    """Список из двух элементов должен вернуть второй элемент"""
    head = linked_list_from_array([1, 2])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 2


def test_three_elements():
    """Список из трех элементов должен вернуть второй элемент (середину)"""
    head = linked_list_from_array([1, 2, 3])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 2


def test_four_elements():
    """Список из четырех элементов должен вернуть третий элемент"""
    head = linked_list_from_array([1, 2, 3, 4])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 3


def test_five_elements():
    """Список из пяти элементов должен вернуть третий элемент (середину)"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 3


def test_six_elements():
    """Список из шести элементов должен вернуть четвертый элемент"""
    head = linked_list_from_array([1, 2, 3, 4, 5, 6])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 4


def test_negative_values():
    """Список с отрицательными значениями должен корректно найти середину"""
    head = linked_list_from_array([-5, -3, -1, 0, 2])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == -1


def test_all_same_values():
    """Список с одинаковыми значениями должен вернуть средний узел"""
    head = linked_list_from_array([7, 7, 7, 7, 7])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 7


def test_large_list_odd():
    """Тест на большом списке с нечетным количеством элементов (99)"""
    arr = list(range(1, 100))
    head = linked_list_from_array(arr)
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 50


def test_large_list_even():
    """Тест на большом списке с четным количеством элементов (100)"""
    arr = list(range(1, 101))
    head = linked_list_from_array(arr)
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 51


def test_middle_node_is_actual_node():
    """Убедиться, что возвращается именно узел списка, а не копия"""
    head = linked_list_from_array([1, 2, 3, 4, 5])
    middle = middle_node(head)
    assert middle is not None
    assert linked_list_to_array(middle) == [3, 4, 5]


def test_slow_fast_pointer_logic():
    """Проверка логики работы медленного и быстрого указателей"""
    head = linked_list_from_array([1, 2, 3, 4, 5, 6, 7])
    middle = middle_node(head)
    assert middle is not None
    assert middle.val == 4