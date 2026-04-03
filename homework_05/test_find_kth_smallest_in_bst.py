"""Тесты для поиска K-ого наименьшего в BST"""
from homework_05.solutions import find_kth_smallest_in_bst, TreeNode


class TestFindKthSmallestInBST:
    def test_empty_tree(self):
        """Пустое дерево"""
        assert find_kth_smallest_in_bst(None, 1) == -1

    def test_single_node(self):
        """Одна вершина"""
        root = TreeNode(5)
        assert find_kth_smallest_in_bst(root, 1) == 5

    def test_bst_k_equals_1(self):
        """K = 1, ищем минимум"""
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.left.right = TreeNode(2)
        assert find_kth_smallest_in_bst(root, 1) == 1

    def test_bst_k_in_middle(self):
        """K в середине"""
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.left.right = TreeNode(2)
        assert find_kth_smallest_in_bst(root, 2) == 2
        assert find_kth_smallest_in_bst(root, 3) == 3

    def test_bst_k_out_of_range(self):
        """K больше контрольного размера дерева"""
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        assert find_kth_smallest_in_bst(root, 10) == -1

    def test_bst_balanced(self):
        """Балансированное BST"""
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        assert find_kth_smallest_in_bst(root, 1) == 1
        assert find_kth_smallest_in_bst(root, 4) == 4
        assert find_kth_smallest_in_bst(root, 7) == 7
