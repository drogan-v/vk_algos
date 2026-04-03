"""Тесты для зеркального отражения дерева"""
from homework_05.solutions import mirror_tree, TreeNode


class TestMirrorTree:
    def test_empty_tree(self):
        """Пустое дерево"""
        assert mirror_tree(None) is None

    def test_single_node(self):
        """Одна вершина"""
        root = TreeNode(1)
        result = mirror_tree(root)
        assert result.val == 1
        assert result.left is None
        assert result.right is None

    def test_two_nodes(self):
        """Два узла"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        mirror_tree(root)
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2

    def test_balanced_tree_mirror(self):
        """Зеркальное отражение балансированного дерева"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        mirror_tree(root)

        assert root.right.val == 2
        assert root.left.val == 3
        assert root.right.left.val == 5
        assert root.right.right.val == 4

    def test_mirror_twice_returns_original(self):
        """Дважды примененное отражение возвращает исходное дерево"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)

        original_left_val = root.left.val
        original_right_val = root.right.val

        mirror_tree(root)
        mirror_tree(root)

        assert root.left.val == original_left_val
        assert root.right.val == original_right_val
