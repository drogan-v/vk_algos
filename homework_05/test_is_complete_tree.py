"""Тесты для проверки полноты дерева"""
from homework_05.solutions import is_complete_tree, TreeNode


class TestIsCompleteTree:
    def test_empty_tree(self):
        """Пустое дерево — полное"""
        assert is_complete_tree(None) is True

    def test_single_node(self):
        """Одна вершина — полное дерево"""
        root = TreeNode(1)
        assert is_complete_tree(root) is True

    def test_complete_tree(self):
        """Полное дерево"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        assert is_complete_tree(root) is True

    def test_incomplete_tree_gap_in_middle(self):
        """Неполное дерево с дырой в середине"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        assert is_complete_tree(root) is False

    def test_incomplete_tree_right_without_left(self):
        """Неполное дерево: правый child без левого"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        assert is_complete_tree(root) is False
