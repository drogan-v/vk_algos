import heapq
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, 
                 right: Optional['TreeNode'] = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor: Optional[int] = None


def is_complete_tree(root: Optional[TreeNode]) -> bool:
    """
    Проверить, является ли бинарное дерево полным.

    Используем BFS:
    - посещаем узлы по уровням слева направо;
    - как только встретили пустой потомок, все следующие узлы в обходе
      также должны быть пустыми;
    - если после первого None встречается реальный узел, дерево не полное.

    Временная сложность: O(n)
    Пространственная сложность: O(n)
    """
    if not root:
        return True

    queue = deque([root])
    found_none = False

    while queue:
        node = queue.popleft()

        if node is None:
            found_none = True
        else:
            if found_none:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    """
    Объединить K отсортированных массивов в один отсортированный массив.

    Идея: держим в min-heap по одному текущему элементу из каждого массива.
    После извлечения минимума добавляем следующий элемент из того же массива.

    Временная сложность: O(n log k), где n - суммарное число элементов.
    Пространственная сложность: O(k) для heap.
    """
    min_heap: list[tuple[int, int, int]] = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged = []
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged.append(value)

        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged


def find_kth_smallest_array(arr: list[int], k: int) -> int:
    """
    Найти K-ый наименьший элемент в массиве.
    
    Подход: использование max-heap размером k.
    - Добавляем первые k элементов в max-heap (отрицаем для Python min-heap).
    - Для оставшихся элементов: если элемент < верхушка heap, заменяем.
    - Результат: верхушка heap содержит k-ый наименьший.
    
    Временная сложность: O(n log k)
    Пространственная сложность: O(k)
    """
    if k > len(arr) or k <= 0:
        raise ValueError("k должно быть в диапазоне [1, len(arr)]")
    
    # Используем max-heap (отрицаем для Python min-heap)
    max_heap: list[int] = [-x for x in arr[:k]]
    heapq.heapify(max_heap)
    
    for num in arr[k:]:
        if num < -max_heap[0]:  # num < максимум в heap
            heapq.heapreplace(max_heap, -num)
    
    return -max_heap[0]


def find_kth_smallest_in_bst(root: Optional[TreeNode], k: int) -> int:
    """
    Найти K-ый наименьший элемент в бинарном дереве поиска.
    
    Подход: in-order обход (левое поддерево → узел → правое поддерево).
    In-order для BST дает элементы в сортированном порядке.
    Останавливаемся после k-го элемента.
    
    Временная сложность: O(k) + O(log n) на балансировку = O(k) в среднем,O(n) в худшем
    Пространственная сложность: O(h) где h - высота дерева (стек рекурсии)
    """
    counter: list[int] = [0]  # счетчик посещенных узлов
    result: list[int] = []
    
    def inorder(node: Optional[TreeNode]) -> None:
        if not node:
            return
        
        inorder(node.left)
        
        counter[0] += 1
        if counter[0] == k:
            result.append(node.val)
            return
        
        if counter[0] < k:
            inorder(node.right)
    
    inorder(root)
    return result[0] if result else -1


def calculate_balance_factor(root: Optional[TreeNode]) -> int:
    """
    Вычислить balance_factor (разница высот левого и правого поддеревьев)
    для каждого узла дерева.
    
    Balance factor = высота левого поддерева - высота правого поддерева
    
    Подход: post-order обход (левое -> правое -> узел).
    Вычисляем высоту снизу вверх, заполняем balance_factor для каждого узла.
    
    Временная сложность: O(n) - посещаем каждый узел один раз
    Пространственная сложность: O(h) - стек рекурсии
    """
    def get_height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        
        node.balance_factor = left_height - right_height
        
        return 1 + max(left_height, right_height)
    
    get_height(root)
    return 0


def mirror_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Преобразовать бинарное дерево в зеркальное отражение,
    меняя местами левые и правые поддеревья каждого узла.
    
    Подход: pre-order обход (узел -> левое -> правое).
    Для каждого узла меняем местами левое и правое поддеревья.
    
    Корректность: После обхода всех узлов все пары (левое, правое) поменяны,
    что дает полное зеркальное отражение.
    
    Временная сложность: O(n) - посещаем каждый узел один раз
    Пространственная сложность: O(h) - стек рекурсии
    """
    if not root:
        return None
    
    root.left, root.right = root.right, root.left
    
    mirror_tree(root.left)
    mirror_tree(root.right)
    
    return root

