"""Тесты для вычисления balance_factor"""
from homework_05.solutions import calculate_balance_factor, TreeNode


class TestCalculateBalanceFactor:
    def test_empty_tree(self):
        """Пустое дерево"""
        assert calculate_balance_factor(None) == 0

    def test_single_node(self):
        """Одна вершина"""
        root = TreeNode(1)
        calculate_balance_factor(root)
        assert root.balance_factor == 0

    def test_left_heavy_tree(self):
        """Дерево, перетяжеленное влево"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        calculate_balance_factor(root)
        assert root.left.left.balance_factor == 0
        assert root.left.balance_factor == 1
        assert root.balance_factor == 2

    def test_right_heavy_tree(self):
        """Дерево, перетяжеленное вправо"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        calculate_balance_factor(root)
        assert root.right.right.balance_factor == 0
        assert root.right.balance_factor == -1
        assert root.balance_factor == -2

    def test_balanced_tree(self):
        """Полностью балансированное дерево"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        calculate_balance_factor(root)
        assert root.left.balance_factor == 0
        assert root.right.balance_factor == 0
        assert root.balance_factor == 0

    def test_complex_tree(self):
        """Сложное дерево"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.left.left = TreeNode(5)
        calculate_balance_factor(root)
        assert root.left.left.left.balance_factor == 0
        assert root.left.left.balance_factor == 1
        assert root.left.balance_factor == 2
        assert root.balance_factor == 2
