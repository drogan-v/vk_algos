from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val: int | None=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr: list[Optional[int]], i: int) -> Optional[TreeNode]:
    """
    Восстановить бинарное дерево из массива, заданного в level-order.

    Для узла с индексом i:
    - левый потомок находится в позиции 2 * i + 1;
    - правый потомок находится в позиции 2 * i + 2.

    Если в массиве на позиции стоит None, это означает отсутствие узла.
    Узлы создаются рекурсивно и связываются через объекты TreeNode.
    """
    if i >= len(arr) or arr[i] is None:
        return None
    
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)

    return root


def check(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    """
    Рекурсивно сравнить зеркальные поддеревья.

    Для симметрии должны выполняться два условия:
    - значения узлов должны совпадать;
    - левое поддерево одного узла должно совпадать с правым поддеревом другого.
    """
    if (not left and not right):
        return True
    
    if (not left or not right or left.val != right.val):
        return False
    
    return check(left.left, right.right) and check(left.right, right.left)


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Проверить, является ли дерево симметричным относительно центра.

    Сравниваются левое и правое поддеревья корня как зеркальные пары.
    """
    if (not root):
        return True
    
    return check(root.left, root.right)


def minDepth(root: Optional[TreeNode]) -> int:
    """
    Найти минимальную глубину бинарного дерева с помощью BFS.

    Поиск в ширину идет по уровням сверху вниз, поэтому первый найденный
    лист будет ближайшим к корню.
    """
    if not root:
        return 0
        
    queue = deque([(root, 1)])
    
    while queue:
        node, depth = queue.popleft()
        
        if not node.left and not node.right:
            return depth
            
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
            
    return 0


def min_max_product_bst(data: list[int]):
    """
    Восстановить BST из массива и вернуть произведение минимального
    и максимального элементов.

    Для BST минимальный элемент лежит в крайней левой ветви,
    а максимальный - в крайней правой, поэтому поиск крайних узлов
    выполняется за O(h), где h - высота дерева.
    """
    root = build_tree(data, 0)

    if not root:
        return None
        
    min_node = root
    while min_node.left:
        min_node = min_node.left
        
    max_node = root
    while max_node.right:
        max_node = max_node.right
        
    return min_node.val * max_node.val


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Проверить, являются ли два бинарных дерева идентичными.

    Деревья одинаковы, если совпадают:
    - структура;
    - значения всех соответствующих узлов.
    """
    if p is None and q is None:
        return True
        
    if p is None or q is None or p.val != q.val:
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
